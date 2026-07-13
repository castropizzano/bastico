import os
import hashlib
import json
from datetime import datetime

def calculate_fingerprint(filepath):
    """Gera o hash SHA-256 do arquivo lendo em blocos (seguro para arquivos pesados)."""
    sha256 = hashlib.sha256()
    try:
        with open(filepath, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256.update(chunk)
        return sha256.hexdigest()
    except Exception as e:
        return f"ERROR: {str(e)}"

def scan_corpus(corpus_path):
    """Varre passivamente o Corpus e estrutura o Inventory."""
    inventory = {
        "metadata": {
            "corpus_path": os.path.abspath(corpus_path),
            "scanned_at": datetime.now().isoformat(),
            "module": "ᴮᵀObserve",
            "status": "STABLE"
        },
        "artifacts": []
    }

    for root, dirs, files in os.walk(corpus_path):
        for filename in files:
            # Pula arquivos invisíveis do sistema (ex: .DS_Store no Mac)
            if filename.startswith('.'):
                continue
                
            filepath = os.path.join(root, filename)
            
            # Extração de Metadados Físicos
            stats = os.stat(filepath)
            
            artifact = {
                "filename": filename,
                "path": filepath,
                "extension": os.path.splitext(filename)[1].lower(),
                "size_bytes": stats.st_size,
                "fingerprint": calculate_fingerprint(filepath)
            }
            
            inventory["artifacts"].append(artifact)

    return inventory

def main():
    # Caminho temporário para o seu laboratório (ajuste se necessário)
    corpus_path = "./bastico_test_corpus" 
    
    if not os.path.exists(corpus_path):
        print(f"⚠️  BɅSTICOᴮᵀ // Erro: O Corpus '{corpus_path}' não foi encontrado.")
        return

    print(f"BɅSTICOᴮᵀ // Iniciando mapeamento passivo no Corpus: {corpus_path}")
    inventory_data = scan_corpus(corpus_path)
    
    # Consolidando a saída em formato JSON universal
    inventory_file = "Inventory.json"
    with open(inventory_file, "w", encoding="utf-8") as f:
        json.dump(inventory_data, f, indent=4, ensure_ascii=False)
    
    print(f"BɅSTICOᴮᵀ // Inventory consolidado com sucesso: {inventory_file}")
    print(f"BɅSTICOᴮᵀ // Total de Artifacts mapeados: {len(inventory_data['artifacts'])}")

if __name__ == "__main__":
    main()
