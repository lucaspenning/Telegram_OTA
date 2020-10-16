# Gerenciamento de Embarcados com Recurso de OTA & Telegram
## Objetivos
Integrar atualizações OTA(Over-The-Air) juntamente com o Telegram que é um serviço de mensagens instantâneas, onde serão mandados comandos específicos por meio do Telegram e o embarcado irá responder conforme o comando solicitado ou retornara algum erro. Além disso será implementado rotina de atualizações OTA, após ser reiniciado ou caso o embarcado permaneça muito tempo ligado.

## Entradas
São comandos dados através do Telegram, além de um Sensor de Temperatura e humidade, são eles:  
  * Uptime: tempo em atividade do embarcado;
  * Version: verifica a versão do software do embarcado;
  * Sensores: sensores instalados no embarcado;
  * Horário: retorna a hora que está no embarcado;
  * Temperatura: retorna temperatura ambiente em graus;
  * Humidade: retorna à humidade ambiente;
  * Atualizar: embarcado irá se atualizar imediatamente;
  * Reiniciar: embarcado será reiniciado;
  * Log: serão enviados periodicamente informações do embarcado;

## Saida
