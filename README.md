# Gerenciamento de Embarcados com Recurso de OTA & Telegram
## Objetivos
Integrar atualizações OTA(Over-The-Air) juntamente com o Telegram que é um serviço de mensagens instantâneas, onde serão mandados comandos específicos por meio do Telegram e o embarcado irá responder conforme o comando solicitado ou retornara algum erro. Além disso será implementado rotina de atualizações OTA, após ser reiniciado ou caso o embarcado permaneça muito tempo ligado. Também irá sem empregado sensor para monitorar temparatura e humidade a fins de demosntração para funcionalidades.

## Entradas
  * Energia 5V;
  * Conexão Wifi;
  * Sensor de temperatura;
  * Sensode de humidade;
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
  * Monitoramento: iremos conseguir monitorar o status e logs do embarcado pelo celular, através das entradas e saídas descritas acima, evitando assim deslocamento até o mesmo;
  * Controle: iremos conseguir mandar comandos para ser realizados pelo embarcado, e obteremos o retorno de valores e status avisando se ocorreu tudo bem na realização da tarefa;
  * Atualizado: com a implementação do OTA, sempre que obtermos um nova atualização ao ser reiniciado o embarcado irá se encarregar de fazer automaticamente, além de uma rotina de verificações que manterão embarcado sempre atualizado caso seja feita a necessidade de seu funcionamento a todo momento, ou se atualizar até mesmo por comando feito pelo Telegram;
  * Sensoriamento: teremos os valores do sensor pretendido sempre que desejado, muito rapidamente, ou iremos receber um aviso em forma de notificação no Telegram caso algum sensor retorne valores indesejados;
