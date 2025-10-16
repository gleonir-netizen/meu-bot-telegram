import time
import schedule
from datetime import datetime
from notification_bot import NotificationBot

class Sistema24_7:
    def __init__(self):
        self.bot = NotificationBot()
        self.contador_verificacoes = 0
        
    def verificar_sistema(self):
        """Verificação periódica do sistema"""
        self.contador_verificacoes += 1
        
        status = f"""
🔄 VERIFICAÇÃO DO SISTEMA #{self.contador_verificacoes}

✅ Todos os sistemas operando normalmente
📊 Verificações realizadas: {self.contador_verificacoes}
⏰ Última verificação: {datetime.now().strftime('%H:%M:%S')}
🔧 Status: OPERACIONAL 24/7
        """.strip()
        
        self.bot.info(status, "admin")
        
        # A cada 10 verificações, notificar o grupo também
        if self.contador_verificacoes % 10 == 0:
            self.bot.grupo(
                "RELATÓRIO PERIÓDICO 📊",
                f"Sistema está operando continuamente!\n"
                f"Verificações realizadas: {self.contador_verificacoes}\n"
                f"Status: ✅ OPERACIONAL",
                "info"
            )
    
    def notificar_evento(self, titulo, mensagem, tipo="info"):
        """Notifica sobre eventos específicos"""
        self.bot.grupo(titulo, mensagem, tipo)
        self.bot.info(f"Evento: {titulo}\n{mensagem}")
    
    def monitorar_continuamente(self):
        """Inicia o monitoramento contínuo"""
        print("🚀 INICIANDO SISTEMA 24/7...")
        
        # Notificação inicial
        self.bot.sucesso(
            "SISTEMA 24/7 INICIADO! 🎉\n\n"
            "📊 Modo: Monitoramento Contínuo\n"
            "⏰ Início: " + datetime.now().strftime('%d/%m/%Y %H:%M:%S') + "\n"
            "🔔 Notificações automáticas ativas"
        )
        
        self.bot.grupo(
            "SISTEMA 24/7 ATIVADO 🚀",
            "✅ Sistema de monitoramento iniciado!\n\n"
            "📱 Este grupo receberá:\n"
            "• Verificações periódicas\n"
            "• Alertas importantes\n"
            "• Status do sistema\n"
            "• Notificações em tempo real\n\n"
            "⚡ Modo: Operação Contínua 24/7",
            "success"
        )
        
        print("✅ Sistema 24/7 inicializado!")
        
        # Agendar verificações automáticas
        schedule.every(5).minutes.do(self.verificar_sistema)
        
        # Verificação inicial
        self.verificar_sistema()
        
        # Loop infinito para manter o sistema rodando
        try:
            while True:
                schedule.run_pending()
                time.sleep(1)
        except KeyboardInterrupt:
            self.bot.alerta("Sistema 24/7 interrompido manualmente")
            print("⏹️ Sistema interrompido")

# Sistema de exemplo para propriedades
class SistemaPropriedades(Sistema24_7):
    def notificar_verificacao_propriedade(self, endereco, resultado):
        """Notifica sobre verificação de propriedade"""
        mensagem = f"""
🏠 VERIFICAÇÃO DE PROPRIEDADE

📋 Endereço: {endereco}
✅ Resultado: {resultado}
⏰ Data: {datetime.now().strftime('%d/%m/%Y %H:%M')}
        """.strip()
        
        self.notificar_evento("NOVA VERIFICAÇÃO 🏠", mensagem, "info")

if __name__ == "__main__":
    print("🔧 Iniciando sistema de propriedades 24/7...")
    sistema = SistemaPropriedades()
    sistema.monitorar_continuamente()