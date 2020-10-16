# Gerenciamento de Embarcados com Recurso de OTA & Telegram
## Objetivos
Integrar atualizações OTA(Over-The-Air) juntamente com o Telegram que é um serviço de mensagens instantâneas, onde serão mandados comandos específicos por meio do Telegram e o embarcado irá responder conforme o comando solicitado ou retornara algum erro. Além disso será implementado rotina de atualizações OTA, após ser reiniciado ou caso o embarcado permaneça muito tempo ligado. Também irá sem empregado sensor para monitorar temparatura e humidade a fins de demosntração para funcionalidades.

## Entradas
  * Energia 5V;
  * Conexão Wifi;
  * Sensor de temperatura;
  * Sensor de humidade;
  * Comandos por Telegram;
  * Repositório GitHub;

## Saídas
  * Realização de rotinas de atualização;
  * Realização das atividades através de comandos por Telegram;
  * Logs do embarcado;
  * Envio de dados solicitados;

## Funcionalidades
São comandos dados através do Telegram, são eles:  
  * Uptime: tempo em atividade do embarcado;
  * Version: verifica a versão do software do embarcado;
  * Sensores: sensores instalados no embarcado;
  * Horário: retorna a hora que está no embarcado;
  * Temperatura: retorna temperatura ambiente em graus;
  * Humidade: retorna à humidade ambiente;
  * Atualizar: embarcado irá se atualizar imediatamente;
  * Reiniciar: embarcado será reiniciado;
  * Log: serão enviados periodicamente informações do embarcado;
