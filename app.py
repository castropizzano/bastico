import ssl
import certifi
import flet as ft
import json
import os
import shutil
import subprocess
import sys
import asyncio

# Contexto SSL escopado (não substitui o contexto global do processo)
SSL_CONTEXT = ssl.create_default_context(cafile=certifi.where())


def load_duplicates():
    """Lê o Inventory.json e agrupa os Artifacts por Fingerprint,
    ordenando cada grupo deterministicamente por path (SPEC_QUARANTINE §2)."""
    try:
        with open("Inventory.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        return None, None

    corpus_path = data.get("metadata", {}).get("corpus_path", os.getcwd())

    groups = {}
    for artifact in data.get("artifacts", []):
        fp = artifact["fingerprint"]
        groups.setdefault(fp, []).append(artifact)

    duplicates = {
        fp: sorted(items, key=lambda a: a["path"])
        for fp, items in groups.items()
        if len(items) > 1
    }
    return duplicates, corpus_path


def quarantine_dir_for(corpus_path):
    """Diretório de quarentena como irmão do Corpus (SPEC_QUARANTINE §2)."""
    parent = os.path.dirname(os.path.abspath(corpus_path))
    return os.path.join(parent, "_QUARENTENA_BASTICO")


def main(page: ft.Page):
    page.title = "BɅSTICOᴮᵀ // Knowledge. Refined."
    page.window.width = 1000
    page.window.height = 700
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 40
    page.bgcolor = "#0D0D0D"
    page.scroll = ft.ScrollMode.AUTO

    async def on_rescan(e):
        btn_rescan.content.value = "Escaneando o Caos..."
        btn_rescan.bgcolor = ft.Colors.BLUE_900
        page.update()

        await asyncio.to_thread(subprocess.run, [sys.executable, "observe.py"])

        build_workspace()
        btn_rescan.content.value = "Re-escanear Corpus"
        btn_rescan.bgcolor = ft.Colors.WHITE10
        page.update()

    btn_rescan = ft.Container(
        content=ft.Text("Re-escanear Corpus", color=ft.Colors.WHITE, size=12, weight=ft.FontWeight.BOLD),
        bgcolor=ft.Colors.WHITE10,
        padding=10,
        border_radius=5,
        ink=True,
        on_click=on_rescan
    )

    header = ft.Column([
        ft.Row([
            ft.Column([
                ft.Text("BɅSTICOᴮᵀ", size=32, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                ft.Text("Módulo de Quarentena", size=14, color=ft.Colors.WHITE54, italic=True),
            ]),
            btn_rescan
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN, vertical_alignment=ft.CrossAxisAlignment.CENTER),
        ft.Divider(height=40, color=ft.Colors.WHITE24)
    ])

    workspace = ft.Column(spacing=20)

    def build_workspace():
        workspace.controls.clear()
        duplicates_data, corpus_path = load_duplicates()

        if duplicates_data is None:
            workspace.controls.append(ft.Text("Erro: Inventory.json não encontrado.", color=ft.Colors.RED))
            page.update()
            return
        if not duplicates_data:
            workspace.controls.append(ft.Text("Nenhuma redundância encontrada. Seu Corpus está limpo.", color=ft.Colors.GREEN))
            page.update()
            return

        workspace.controls.append(
            ft.Text(f"Encontrados {len(duplicates_data)} grupos de artefatos idênticos:",
                    color=ft.Colors.WHITE70, weight=ft.FontWeight.BOLD)
        )

        q_dir = quarantine_dir_for(corpus_path)

        for fp, items in duplicates_data.items():
            group_container = ft.Container(
                bgcolor="#1A1A1A", padding=20, border_radius=10, content=ft.Column()
            )
            group_container.content.controls.append(
                ft.Text(f"Fingerprint: {fp[:16]}...", size=12, color=ft.Colors.WHITE38, font_family="monospace")
            )
            group_container.content.controls.append(ft.Divider(height=10, color=ft.Colors.WHITE10))

            files_column = ft.Column()
            files_scrollable_row = ft.Row([files_column], scroll=ft.ScrollMode.AUTO)

            row_refs = {}
            for i, item in enumerate(items):
                is_reference = (i == 0)
                icon = ft.Icons.CHECK_CIRCLE if is_reference else ft.Icons.FILE_COPY
                icon_color = ft.Colors.GREEN_400 if is_reference else ft.Colors.WHITE54
                label = "REFERÊNCIA: " if is_reference else "REDUNDÂNCIA: "
                text_color = ft.Colors.WHITE if is_reference else ft.Colors.WHITE54

                status_text = ft.Text("", size=11, color=ft.Colors.WHITE38)
                file_row = ft.Row([
                    ft.Icon(icon, size=16, color=icon_color),
                    ft.Text(f"{label}{item['path']}", size=14, color=text_color, selectable=True, no_wrap=True),
                    status_text
                ])
                files_column.controls.append(file_row)
                if not is_reference:
                    row_refs[item["path"]] = status_text

            group_container.content.controls.append(files_scrollable_row)

            def make_isolate_action(current_items, current_status_refs, current_q_dir):
                def on_isolate(e):
                    os.makedirs(current_q_dir, exist_ok=True)
                    redundancies = current_items[1:]
                    for copy in redundancies:
                        src = copy["path"]
                        status = current_status_refs.get(src)
                        if not os.path.exists(src):
                            if status:
                                status.value = "já isolado"
                                status.color = ft.Colors.WHITE38
                            continue
                        try:
                            filename = os.path.basename(src)
                            dest = os.path.join(current_q_dir, f"{copy['fingerprint'][:8]}_{filename}")
                            shutil.move(src, dest)
                            if status:
                                status.value = "isolado ✓"
                                status.color = ft.Colors.GREEN_400
                        except Exception as ex:
                            if status:
                                status.value = f"erro: {str(ex)[:40]}"
                                status.color = ft.Colors.ORANGE_400
                    e.control.content.value = "Isolamento Concluído"
                    e.control.bgcolor = ft.Colors.GREEN_900
                    e.control.disabled = True
                    page.update()
                return on_isolate

            btn_isolate = ft.Container(
                content=ft.Text("Isolar Redundâncias", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD),
                bgcolor=ft.Colors.BLUE_900, padding=10, border_radius=5, ink=True,
                on_click=make_isolate_action(items, row_refs, q_dir)
            )

            actions = ft.Row([btn_isolate], alignment=ft.MainAxisAlignment.END)
            group_container.content.controls.append(ft.Container(height=10))
            group_container.content.controls.append(actions)
            workspace.controls.append(group_container)

        page.update()

    build_workspace()
    page.add(header, workspace)


if __name__ == "__main__":
    ft.run(main)
