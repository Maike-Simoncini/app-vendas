{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "toc_visible": true,
      "authorship_tag": "ABX9TyP1iBBPbJwJqIYMehdDgBuS",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Maike-Simoncini/app-vendas/blob/main/Untitled0.pc\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "_VwEhHHlTTWV"
      },
      "outputs": [],
      "source": [
        "print('Bem vindo a loja do Maike Simoncini da Silva') # identificador pessoal\n",
        "valor_produto = float(input('Entre com valor do produto: ')) # entrada valor do produto\n",
        "quant_produto = int(input('Entre com valor da quantidade: ')) # entrada quantidade do produto\n",
        "desconto_produto = 0 # variável desconto\n",
        "# desconto por quantidade de produto\n",
        "if quant_produto <= 9: \n",
        "  desconto_produto = 0.00 # 0% de desconto\n",
        "elif quant_produto >= 10 and quant_produto <= 99: \n",
        "  desconto_produto = 0.05 # 5% de desconto\n",
        "elif quant_produto >= 100 and quant_produto <= 999: \n",
        "  desconto_produto = 0.10 # 10% de desconto\n",
        "else: \n",
        "  desconto_produto = 0.15 # 15% de desconto\n",
        "total_desconto = int(desconto_produto * 100)\n",
        "total_sem_desconto = valor_produto * quant_produto # variável total de produto sem desconto\n",
        "print('O valor sem desconto foi: R$ {:.2f}'.format(total_sem_desconto)) # saída do total sem desconto\n",
        "total_com_desconto = total_sem_desconto - total_sem_desconto * desconto_produto # variável total de produto com desconto\n",
        "print('O valor com desconto foi: R$ {:.2f} (desconto {}%)'.format(total_com_desconto,total_desconto)) # saída total com desconto"
      ]
    }
  ]
}
