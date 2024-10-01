# Ferramenta de Renomeação em Massa de Arquivos
Descrição
Esta ferramenta permite renomear múltiplos arquivos em massa com base em uma planilha que especifica o nome atual e o novo nome de cada arquivo. Ideal para quem precisa gerenciar grandes volumes de arquivos de maneira rápida e eficiente.

## Como Utilizar
1. Preparação
Pasta com Arquivos: Tenha em mãos o endereço da pasta onde os arquivos a serem renomeados estão localizados.
Planilha de Nomes: Prepare uma planilha em formato .xlsx com duas colunas:
nome_atual: o nome atual do arquivo (incluindo a extensão, como .mp4).
novo_nome: o novo nome desejado para o arquivo (também com a extensão).
2. Execução
Abrir a ferramenta: Execute o arquivo da ferramenta para iniciar o programa.
Selecionar a pasta: Ao abrir a ferramenta, você verá um botão chamado "Selecionar Pasta". Clique nele e escolha a pasta que contém os arquivos a serem renomeados.
Após selecionar a pasta, a ferramenta exibirá todos os arquivos da pasta em uma tabela, incluindo uma coluna com o ID de cada arquivo, facilitando a contagem e identificação.
Carregar os novos nomes: Clique no botão "Encontrar Nomes" para selecionar a planilha com os nomes. A ferramenta exibirá uma terceira coluna na tabela com o novo nome proposto para cada arquivo.
Verificar os novos nomes: Revise a lista de novos nomes na tabela para garantir que estejam corretos.
Renomear os arquivos: Após confirmar os novos nomes, clique em "Renomear Arquivos". A ferramenta renomeará os arquivos de acordo com o que foi especificado.
3. Finalização
Após o processo de renomeação, uma mensagem de confirmação será exibida.
Em caso de erros (por exemplo, se um arquivo não for encontrado ou a planilha tiver nomes incorretos), a ferramenta notificará o erro e registrará o problema em um log.

## Observações Importantes
### Nomes Precisos: O nome atual dos arquivos deve estar exatamente igual ao nome original na planilha, incluindo a extensão (por exemplo, .mp4, .avi). Se o nome ou a extensão estiverem incorretos, o arquivo não será renomeado corretamente.
Mudança de Extensão: Evite alterar a extensão do arquivo (exemplo: de .mp4 para .avi), pois isso pode corromper o arquivo.
### Dica Rápida: Para copiar facilmente os nomes dos arquivos de uma pasta:
Abra a pasta onde os arquivos estão.
Clique com o botão direito do mouse em um espaço vazio e selecione "Abrir no terminal".
No terminal, digite o comando dir para listar todos os arquivos.
Copie a lista de arquivos exibida e cole no Excel. Use a função "Texto para Colunas" com a opção de "largura fixa" para ajustar os nomes.
Com isso, você poderá criar a planilha necessária com o nome atual e o novo nome, sempre garantindo que a extensão do arquivo (.mp4, .avi, etc.) esteja correta em ambas as colunas.
