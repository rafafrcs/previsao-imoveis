# Previsão de Valor de Imóveis

Este é um projeto em Python usando Flask para criar uma aplicação web que estima o valor de um imóvel com base em características fornecidas pelo usuário. O modelo de previsão foi treinado com dados reais e usa Gradient Boosting Regressor.

## Funcionalidades
- Formulário em interface web (HTML + Tailwind CSS)
- Previsão de valor com base em 17 características do imóvel
- Preenchimento automático de campos com médias quando deixados em branco
- Relatório resumido com os dados inseridos e auto-preenchidos

## Tecnologias utilizadas
- Python
- Flask
- Pandas
- Scikit-learn
- Tailwind CSS

## Estrutura do projeto
```
projeto-imoveis/
├── app.py                     # Servidor Flask
├── modelo_imoveis.pkl        # Modelo treinado (pickle)
├── mean_values.json          # Médias dos campos usados
├── dataset/ukc_house_data.csv# Dataset original
├── templates/index.html      # Template HTML com Tailwind
├── static/estilo.css         # (opcional) Arquivo CSS adicional
├── requirements.txt          # Dependências
└── README.md                 # Este arquivo
```

## Como executar localmente
1. Clone o repositório:
```bash
git clone https://github.com/SEU_USUARIO/previsao-imoveis.git
cd previsao-imoveis
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute o servidor:
```bash
python app.py
```

4. Acesse no navegador:
```
http://localhost:5000
```

## Licença
Este projeto é livre para fins educacionais.