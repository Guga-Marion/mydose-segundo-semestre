# -*- coding: utf-8 -*-
from blocks import h2, h3, p, ul, ol, callout, contact

UPDATED = {"pt":"16 de junho de 2026","en":"June 16, 2026","es":"16 de junio de 2026"}

CAP = {  # rótulo "Capítulo" por idioma
  "pt":"Capítulo","en":"Chapter","es":"Capítulo"
}

def _toc(lang):
    T = {
      "pt":["Disposições Gerais","Informações Coletadas","Como Usamos as Informações","Compartilhamento de Informações","Cookies","Acesso e Correção","Notificação de Modificações","Inteligência Artificial (IA)","Uso de E-mail","Proibições","Segurança das Informações","Marketing Digital","Contato","Google User Data — Limited Use"],
      "en":["General Provisions","Information Collected","How We Use Information","Sharing of Information","Cookies","Access and Correction","Notification of Changes","Artificial Intelligence (AI)","Use of E-mail","Prohibitions","Security of Information","Digital Marketing","Contact","Google User Data — Limited Use"],
      "es":["Disposiciones Generales","Información Recopilada","Cómo Usamos la Información","Compartición de Información","Cookies","Acceso y Corrección","Notificación de Cambios","Inteligencia Artificial (IA)","Uso de E-mail","Prohibiciones","Seguridad de la Información","Marketing Digital","Contacto","Google User Data — Limited Use"],
    }
    return [("ch%d"%(i+1), lbl) for i,lbl in enumerate(T[lang])]

def build_pt():
    C=CAP["pt"]; b=""
    b+=p("Olá Usuário, obrigado por acessar o aplicativo MyDose. A My Dose LLC tem o compromisso de cumprir as leis que protegem a privacidade dos dados dos Usuários e do público em geral. Para prestar os serviços relacionados ao aplicativo MyDose, é necessário tratar e compartilhar dados pessoais. AO UTILIZAR O APLICATIVO MYDOSE, O USUÁRIO CONCORDA TÁCITA E INTEGRALMENTE COM AS DISPOSIÇÕES AQUI CONTIDAS.", lead=True)
    b+=h2("Disposições Gerais","ch1",cap=C+" I")
    b+=p("1.1. O aplicativo MyDose considera de extrema importância o relacionamento com seus Usuários e seus dados pessoais. Esta Política de Privacidade foi elaborada para comunicar nossas práticas de coleta, uso e divulgação de informações.")
    b+=p("1.2. Informações pessoais são dados fornecidos pelos Usuários que podem ser utilizados para identificá-los individualmente.")
    b+=p("1.3. Informações pessoais sensíveis incluem dados sobre origem racial ou étnica, convicções religiosas, opiniões políticas e dados de saúde, conforme estipulado pela Lei 13.709/18 (LGPD).")
    b+=p("1.4. AO UTILIZAR O APLICATIVO MYDOSE, VOCÊ AUTORIZA A COLETA, O USO E A DIVULGAÇÃO DE INFORMAÇÕES SOBRE VOCÊ, NOS TERMOS DESTA POLÍTICA.")
    b+=p("1.5. O aplicativo MyDose opera em conformidade com a legislação brasileira, incluindo a Lei nº 12.965/2014 (Marco Civil da Internet) e a Lei nº 13.709/2018 (LGPD).")
    b+=p('1.6. Em caso de dúvidas, entre em contato pelo e-mail <a class="inl" href="mailto:contact@mydoseapp.com">contact@mydoseapp.com</a>.')
    b+=p("1.7. Esta Política descreve quais informações podem ser coletadas sobre os Usuários e como podem ser utilizadas.")
    b+=h2("Informações Coletadas","ch2",cap=C+" II")
    b+=p("2.1. Dados coletados dos Usuários:")
    b+=ul(["Nome completo","Endereço de e-mail válido","Data de nascimento","Idade","Informações de saúde física, bem-estar mental, orçamento pessoal e nutrição"])
    b+=p("2.1.1. Os dados pessoais são coletados em diversas circunstâncias, incluindo cadastro no aplicativo e ativação de funcionalidades.")
    b+=p("2.1.2. Dados pessoais sensíveis também são coletados, tais como dados de atividade física, informações médicas e de saúde provenientes de dispositivos conectados (Google Fit, Apple Health, Samsung Health, Strava, Garmin etc.).")
    b+=p("2.1.3. Os Usuários podem optar por conectar e compartilhar informações de aplicativos parceiros com o MyDose.")
    b+=p("2.1.4. As informações coletadas por parceiros e terceiros estão sujeitas aos seus próprios termos e políticas.")
    b+=p("2.2. Dados coletados dos Usuários Líderes:")
    b+=ul(["Nome completo","Endereço de e-mail válido","Telefone","CPF ou CNPJ","Endereço completo","Dados de cartão de crédito"])
    b+=p("2.3. A coleta de dados de menores será realizada mediante consentimento do Responsável.")
    b+=p('2.4. <strong>Dados obtidos por meio das APIs do Google.</strong> Quando um Usuário Líder opta por conectar sua conta Google, o MyDose solicita acesso aos seguintes escopos da API do Google:')
    b+=ul(['<code>https://www.googleapis.com/auth/calendar.events</code> — para criar eventos de calendário (com link do Google Meet) no Google Calendar do profissional quando uma consulta online é agendada na plataforma.',
           '<code>https://www.googleapis.com/auth/userinfo.email</code> — para identificar e exibir qual conta Google foi conectada.'])
    b+=p('O tratamento de todos os dados obtidos por meio dessas APIs do Google é regido exclusivamente pelo <strong>Capítulo XIV (Google User Data — Limited Use)</strong> abaixo, que prevalece sobre qualquer disposição em contrário nesta Política.')
    b+=h2("Como Usamos as Informações","ch3",cap=C+" III")
    b+=p("3.1. O MyDose utiliza as informações coletadas para:")
    b+=ul(["a) Identificar e cadastrar Usuários e prestar os serviços do aplicativo","b) Garantir que o conteúdo seja apresentado da forma mais eficiente","c) Realizar melhorias gerais no aplicativo","d) Oferecer a Administradores de RH acesso aos dados para análises e relatórios","e) Contatar e notificar Usuários sobre mudanças na plataforma","f) Conduzir pesquisas estatísticas","g) Alimentar o banco de dados Data Lake do MyDose","h) Fins promocionais ou de marketing","i) Desenvolver soluções personalizadas para uma vida mais saudável"])
    b+=p("3.2. Informações adicionais não pessoais podem ser utilizadas para qualquer finalidade.")
    b+=p("3.3. <strong>O MYDOSE MANTÉM REGISTROS DE ACESSO À INTERNET SOB SIGILO, EM AMBIENTE CONTROLADO E SEGURO, COM CRIPTOGRAFIA EM TRÂNSITO.</strong>")
    b+=p("3.4. Informações médicas sensíveis não serão usadas em decisões futuras de subscrição ou sinistros.")
    b+=p("3.5. Os serviços do MyDose não se destinam a diagnosticar, curar, mitigar, tratar ou prevenir qualquer condição, nem substituem o cuidado médico profissional.")
    b+=p("3.6. Os usos descritos nos itens 3.1(d), 3.1(f), 3.1(g), 3.1(h) e 3.2 NÃO se aplicam aos dados obtidos por meio das APIs do Google. Esses dados são utilizados unicamente conforme descrito no Capítulo XIV.")
    b+=h2("Compartilhamento de Informações","ch4",cap=C+" IV")
    b+=p("4.1. O MyDose não divulga a terceiros qualquer informação fornecida pelo Usuário, exceto:")
    b+=ul(["a) Para cumprir obrigação legal ou prevenir fraudes","b) Para proteger os direitos, propriedade ou segurança do MyDose","c) Com autoridades policiais ou governamentais","d) Mediante notificação e consentimento prévios do Usuário","e) Por ação do próprio Usuário, como o compartilhamento com Líderes de Comunidade","f) Para pesquisa estatística ou autoral","g) Com empresas terceirizadas prestadoras de serviços em conformidade com padrões de privacidade","h) Com agentes, contratados ou prestadores de serviços terceirizados","i) Com servidores terceirizados contratados que armazenam o banco de dados (Google Cloud Platform, Supabase)","j) Em caso de venda, fusão ou reestruturação empresarial"])
    b+=p("4.2. <strong>Compartilhamento internacional.</strong> O MyDose utiliza serviços do Google Cloud Platform para armazenar e processar dados, que podem ser transferidos para os Estados Unidos.")
    b+=p("4.3. <strong>Compartilhamento com IA.</strong> Os dados dos Usuários (excluídos os dados obtidos por meio das APIs do Google) podem ser compartilhados via integração de API com o Gemini (Google AI) para relatórios, automação de processos e interações automatizadas. Os dados obtidos por meio das APIs do Google nunca são transmitidos para serviços de IA, conforme o Capítulo XIV.")
    b+=p("4.4. <strong>Não divulgação.</strong> Exceto nas situações acima, o MyDose não divulgará qualquer informação pessoal.")
    b+=p("4.5. O USUÁRIO TEM O DIREITO DE NÃO ACEITAR ESTES TERMOS E DE REMOVER SEUS DADOS.")
    b+=p("4.6. Ao aceitar estes termos, o Usuário autoriza o compartilhamento de dados. O Usuário pode revogar o consentimento a qualquer momento, inclusive desconectando sua conta Google.")
    b+=p("4.7. O MyDose manterá os dados do Usuário enquanto este estiver cadastrado ou enquanto houver legítimo interesse da empresa.")
    b+=p("4.8. O compartilhamento permitido pelos itens 4.1(f), 4.1(g), 4.1(h) e 4.3 NÃO se aplica aos dados obtidos por meio das APIs do Google, exceto quando estritamente necessário para prover a funcionalidade voltada ao usuário, conforme detalhado no Capítulo XIV.")
    b+=h2("Cookies","ch5",cap=C+" V")
    b+=p("5.1. Cookie é uma informação armazenada localmente no dispositivo do Usuário contendo dados sobre suas atividades na Internet.")
    b+=p("5.2. Cookies utilizados:")
    b+=ul(["<strong>Cookies de Desempenho:</strong> coletam informações anônimas sobre o uso da plataforma","<strong>Cookies Funcionais:</strong> proporcionam melhor experiência de navegação"])
    b+=p("5.3. O acesso aos cookies termina quando o Usuário fecha o navegador. Você pode aceitar ou recusar cookies nas configurações do navegador.")
    b+=p("5.4. A aceitação do Usuário é necessária antes do uso de cookies.")
    b+=p("5.5. Caso opte por recusar cookies, o acesso à maior parte das informações disponíveis pode ser comprometido.")
    b+=h2("Acesso e Correção de Informações Pessoais","ch6",cap=C+" VI")
    b+=p("6.1. O MyDose adotará todas as medidas adequadas para atualizar e corrigir informações pessoais identificáveis.")
    b+=p("6.2. O Usuário tem o direito de acessar, modificar, corrigir e excluir seus dados a qualquer momento.")
    b+=p("6.3. É responsabilidade do Usuário manter suas informações pessoais atualizadas.")
    b+=p("6.3.1. O Usuário é responsável pelas informações inseridas no aplicativo, afirmando que revisou sua precisão, inclusive quando as informações forem extraídas por inteligência artificial.")
    b+=p('6.4. O Usuário tem o direito de acessar suas informações pessoais nos termos da Lei nº 12.965/2014 e da Lei nº 13.709/2018, contatando <a class="inl" href="mailto:contact@mydoseapp.com">contact@mydoseapp.com</a>.')
    b+=p("6.5. O MyDose adota todas as medidas necessárias para proteger as informações pessoais contra perda, uso indevido e acesso não autorizado, com criptografia e padrões rigorosos de segurança.")
    b+=p("6.6. O Usuário é responsável pela proteção de suas senhas e recursos de acesso.")
    b+=h2("Notificação de Modificações da Política de Privacidade","ch7",cap=C+" VII")
    b+=p("7.1. O MyDose pode alterar a Política de Privacidade periodicamente. Caso ocorram mudanças no uso de informações pessoais, os Usuários serão notificados por anúncios na plataforma ou por e-mail.")
    b+=p("7.2. O uso continuado dos serviços após qualquer alteração constitui aceitação da Política modificada.")
    b+=p("7.3. Ajustes menores podem ocorrer sem notificação prévia.")
    b+=h2("Uso de Funcionalidades de Inteligência Artificial (IA)","ch8",cap=C+" VIII")
    b+=p("Nosso aplicativo pode oferecer funcionalidades opcionais baseadas em serviços de Inteligência Artificial de terceiros (por exemplo, Gemini / Google AI) para auxiliar na geração de resumos ou sugestões de saúde.")
    b+=p("<strong>Compartilhamento de dados:</strong> Ao optar por usar essas funcionalidades, entradas de texto específicas ou dados explicitamente selecionados por você podem ser transmitidos ao provedor de IA para processamento. Os dados obtidos por meio das APIs do Google (como dados do Google Calendar) são excluídos e nunca são transmitidos a serviços de IA.")
    b+=p("<strong>Consentimento:</strong> Ao usar essas funcionalidades de IA, você consente com essa transferência de dados.")
    b+=p("<strong>Aviso:</strong> Todo conteúdo gerado por IA tem caráter meramente informativo e é revisado pelo seu profissional de saúde. Não constitui aconselhamento médico.")
    b+=p("<strong>Retenção de dados:</strong> Não permitimos que provedores de IA de terceiros utilizem seus dados pessoais para treinar seus modelos.")
    b+=h2("Uso de E-mail","ch9",cap=C+" IX")
    b+=p("9.1. Ao se cadastrar, o Usuário concorda em receber notificações, novidades e informações importantes por e-mail.")
    b+=p('9.1.1. O Usuário pode optar por sair utilizando o opt-out ou solicitando a remoção via <a class="inl" href="mailto:contact@mydoseapp.com">contact@mydoseapp.com</a>.')
    b+=p("9.1.2. E-mails administrativos relacionados à manutenção da conta não podem ser cancelados.")
    b+=p("9.1.3. O uso do MyDose para Spam é absolutamente proibido.")
    b+=p("9.2. É garantido sigilo máximo no tratamento dos endereços de e-mail dos Usuários.")
    b+=p("9.2.1. É garantida ao Usuário a possibilidade de remover seu endereço de e-mail.")
    b+=h2("Proibições","ch10",cap=C+" X")
    b+=p("10.1. O MyDose reserva-se o direito de recusar ou remover qualquer conexão que contenha informações incorretas ou afirmações sem fundamento.")
    b+=h2("Segurança das Informações Pessoais","ch11",cap=C+" XI")
    b+=p("11.1. O aplicativo MyDose utiliza criptografia de dados. As informações são hospedadas em servidores nos Estados Unidos, com acesso apenas por funcionários autorizados.")
    b+=p("11.2. Se o MyDose tomar conhecimento de qualquer violação de segurança, notificará imediatamente os Usuários afetados.")
    b+=p("11.3. O MyDose pode copiar, divulgar, distribuir, incorporar e usar materiais e dados para fins comerciais ou não comerciais, respeitando esta Política. <strong>Esta disposição NÃO se aplica aos dados obtidos por meio das APIs do Google, que são regidos exclusivamente pelo Capítulo XIV.</strong>")
    b+=p("11.4. O Usuário será responsável por indenizar o MyDose pelos custos decorrentes de violações desta Política.")
    b+=p("11.5. O MyDose coopera com autoridades que solicitem a identificação de pessoas que violem estas disposições.")
    b+=p("11.6. Esta Política trata apenas do uso e divulgação de informações coletadas pelo MyDose. O MyDose não controla políticas de privacidade de terceiros.")
    b+=h2("Marketing Digital","ch12",cap=C+" XII")
    b+=p('12.1. Ao aderir ao aplicativo MyDose, o Usuário compreende e reconhece que o MyDose pode enviar comunicações de marketing por redes sociais como Facebook, Instagram, Google, LinkedIn etc. O MyDose também pode entrar em contato com os Usuários via WhatsApp. O Usuário pode optar por sair das comunicações de marketing enviando solicitação para <a class="inl" href="mailto:contact@mydoseapp.com">contact@mydoseapp.com</a>.')
    b+=p("12.2. <strong>Os dados obtidos por meio das APIs do Google nunca são usados para marketing, publicidade ou qualquer finalidade promocional, conforme o Capítulo XIV.</strong>")
    b+=h2("Contato","ch13",cap=C+" XIII")
    b+=p("13.1. O Usuário pode contatar o MyDose a qualquer momento para compartilhar opiniões sobre práticas de privacidade ou dúvidas relacionadas às suas informações pessoais:")
    b+=contact([("E-mail",'<a href="mailto:contact@mydoseapp.com">contact@mydoseapp.com</a>'),("Telefone","+1 424-537-2605"),("Endereço","Los Angeles, Califórnia — EUA")])
    b+=h2("Google User Data — Limited Use","ch14",cap=C+" XIV")
    b+=p("O uso e a transferência, pelo MyDose, de quaisquer informações recebidas das APIs do Google — incluindo os escopos <code>calendar.events</code> e <code>userinfo.email</code> — obedecem à Google API Services User Data Policy, incluindo os requisitos de Limited Use.")
    b+=p("Especificamente, <strong>os dados obtidos por meio das APIs do Google são utilizados unicamente para prover e melhorar as funcionalidades voltadas ao usuário</strong> para as quais o usuário concedeu acesso. O escopo <code>calendar.events</code> é usado apenas para criar eventos de calendário (com link do Google Meet) no Google Calendar do profissional quando uma consulta online é agendada na plataforma. O escopo <code>userinfo.email</code> é usado apenas para identificar e exibir qual conta Google foi conectada.")
    b+=p("O MyDose não:")
    b+=ul(["utiliza dados de usuários do Google para publicidade, marketing ou qualquer finalidade promocional;","vende dados de usuários do Google, nem os transfere a terceiros, exceto quando necessário para prover ou melhorar a funcionalidade voltada ao usuário, para cumprir lei aplicável, ou como parte de fusão ou aquisição com aviso ao usuário;","usa ou transfere dados de usuários do Google para desenvolver, melhorar ou treinar modelos generalizados ou não personalizados de inteligência artificial e/ou aprendizado de máquina, incluindo serviços de IA de terceiros como o Gemini;","permite que humanos leiam dados de usuários do Google, exceto quando: (a) o usuário fornecer consentimento prévio explícito; (b) for necessário para fins de segurança; (c) for exigido para cumprir lei aplicável; ou (d) os dados estiverem agregados e anonimizados e forem usados para operações internas."])
    b+=p("Este Capítulo XIV prevalece sobre qualquer disposição em contrário desta Política. As disposições dos Capítulos III, IV, VIII, XI e XII relativas a marketing, agregação de dados, Data Lake, uso comercial, compartilhamento com terceiros e processamento por IA não se aplicam aos dados obtidos por meio das APIs do Google.")
    b+=p("Os usuários podem revogar, a qualquer momento, o acesso do MyDose aos seus dados Google desconectando sua conta Google dentro do aplicativo, ou pela página de permissões da Conta Google.")
    b+=callout("Google API Services User Data Policy","<p>MyDose's use and transfer of information received from Google APIs to any other app will adhere to the <a class='inl' href='https://developers.google.com/terms/api-services-user-data-policy' target='_blank' rel='noopener'>Google API Services User Data Policy</a>, including the Limited Use requirements. MyDose does not use or transfer data obtained through Google Workspace APIs to develop, improve, or train generalized artificial intelligence and/or machine learning models.</p>", warn=False)
    return b

def content(lang):
    # PT é a fonte; EN/ES importados dos módulos de tradução
    if lang=="pt":
        return UPDATED["pt"], build_pt(), _toc("pt")
    from content_privacidade_tr import build as build_tr
    return UPDATED[lang], build_tr(lang), _toc(lang)
