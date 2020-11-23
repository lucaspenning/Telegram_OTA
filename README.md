# Gerenciamento de Embarcados com Recurso de OTA & Telegram
## Objetivos
Integrar atualizações OTA(Over-The-Air) juntamente com o Telegram que é um serviço de mensagens instantâneas, onde serão mandados comandos específicos por meio do Telegram e o embarcado irá responder conforme o comando solicitado ou retornara algum erro. Além disso será implementado rotina de atualizações OTA, após ser reiniciado ou caso o embarcado permaneça muito tempo ligado. Também irá sem empregado sensor para monitorar temparatura e humidade a fins de demosntração para funcionalidades.

## Entradas
  * Sensor de temperatura;
  * Sensor de humidade;
  * Comandos por Telegram;

## Saídas
  * Realização de rotinas de atualização;
  * Realização das atividades através de comandos por Telegram;
  * Logs do embarcado;
  * Envio de dados solicitados.
  
## Requisitos
  * Alimentação de 5V;
  * Repositório GitHub;
  * Conexão Wifi.

## Funcionalidades
* **Visão Geral:** Será realizado o monitoramento do embarcado pelo Telegram através das funcionalidades descritas abaixo, além de comandos com tarefas para serem realizados pelo embarcado obtendo retorno de valores e status avisando se ocorreu tudo bem nas realizações das mesmas. Com a implementação do OTA sempre que um nova atualização sair, ao ser reiniciado o embarcado irá se encarregar de fazer automaticamente, contamos também com uma rotina de verificações que manterá o embarcado sempre atualizado caso se faça a necessidade de seu funcionamento constantemente, ou também disparando um comando de atualização pelo Telegram. Teremos os valores do sensor pretendido sempre que desejado rapidamente, se necessário um aviso em forma de notificação no Telegram irá informar se algum sensor retorne valores indesejados. 

* **Operações:**
  * Uptime: tempo em atividade do embarcado;
  * Version: verifica a versão do software do embarcado;
  * Sensores: sensores instalados no embarcado;
  * Horário: retorna a hora que está no embarcado;
  * Temperatura: retorna temperatura ambiente em graus;
  * Umidade: retorna à Umidade ambiente;
  * Atualizar: embarcado irá se atualizar imediatamente;
  * Reiniciar: embarcado será reiniciado;
  * Serão enviadas a cada X minutos as medições do sensores para o BoT Telegram
  * Por padrão X = 30 minutos, podendo ser configurado um novo valor por mensagem
  * Registrar no embarcado o histórico das atualizações: versão e data
  * Registrar no embarcado um log das últimas 24h das medições feitas pelos sensores
  * Por solicitação será enviado o log das últimas 24h das medições feitas
  * Por solicitação será enviado o histórico das atualizações

## Diagrama UML de Funcionamento
 ![Imagens/Diagrama UML.png]
