import requests
import time
from datetime import datetime
import config

class NotificationBot:
    def __init__(self):
        self.token = config.BOT_TOKEN
        self.admin_id = config.ADMIN_ID
        self.group_id = config.GROUP_ID
    
    def enviar_notificacao(self, titulo, mensagem, tipo="info", destino="admin"):
        """Envia notificação para admin ou grupo"""
        
        emoji = config.NOTIFICATION_TYPES.get(tipo, "📢")
        chat_id = self.admin_id if destino == "admin" else self.group_id
        
        mensagem_formatada = f"""
{emoji} <b>{titulo}</b>

{mensagem}

<code>─────────────────────</code>
<i>Enviado em: {datetime.now().strftime('%d/%m/%Y %H:%M')}</i>
        """.strip()
        
        url = f"https://api.telegram.org/bot{self.token}/sendMessage"
        payload = {
            "chat_id": chat_id,
            "text": mensagem_formatada,
            "parse_mode": "HTML",
            "disable_web_page_preview": True
        }
        
        try:
            response = requests.post(url, json=payload, timeout=10)
            if response.status_code == 200:
                print(f"✅ Notificação enviada para {destino}: {titulo}")
                return True
            else:
                print(f"❌ Erro ao enviar: {response.text}")
                return False
        except Exception as e:
            print(f"❌ Erro: {e}")
            return False
    
    # Métodos rápidos para cada tipo
    def sucesso(self, mensagem, destino="admin"):
        return self.enviar_notificacao("SUCESSO", mensagem, "success", destino)
    
    def erro(self, mensagem, destino="admin"):
        return self.enviar_notificacao("ERRO", mensagem, "error", destino)
    
    def alerta(self, mensagem, destino="admin"):
        return self.enviar_notificacao("ALERTA", mensagem, "alert", destino)
    
    def info(self, mensagem, destino="admin"):
        return self.enviar_notificacao("INFORMAÇÃO", mensagem, "info", destino)
    
    def grupo(self, titulo, mensagem, tipo="info"):
        return self.enviar_notificacao(titulo, mensagem, tipo, "group")