import requests

# Suas configurações
BOT_TOKEN = "8394093109:AAEhnXGb_hOoVG1Squ0sw4QcfmVfWUN6sxs"

def descobrir_grupos():
    """Descobre todos os grupos/chats onde o bot está"""
    print("🔍 Procurando grupos e chats...")
    
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"
    
    try:
        response = requests.get(url, timeout=10)
        dados = response.json()
        
        if dados.get('ok') and dados['result']:
            print("📱 Grupos/Chats encontrados:")
            for update in dados['result']:
                if 'message' in update:
                    chat = update['message']['chat']
                    chat_type = chat['type']  # private, group, supergroup
                    chat_id = chat['id']
                    chat_title = chat.get('title', 'Chat Privado')
                    username = chat.get('username', 'Sem username')
                    
                    print(f"├── 🆔 ID: {chat_id}")
                    print(f"├── 📝 Tipo: {chat_type}")
                    print(f"├── 🏷️ Nome: {chat_title}")
                    print(f"├── 👤 Username: @{username}")
                    print(f"└── {'─' * 30}")
        else:
            print("❌ Nenhuma mensagem encontrada")
            print("💡 Envie uma mensagem no GRUPO para o bot aparecer aqui")
            
    except Exception as e:
        print(f"❌ Erro: {e}")

if __name__ == "__main__":
    descobrir_grupos()