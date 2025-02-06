"""Testes para a interface gráfica (interface.py)"""

import os
import tkinter as tk
from unittest.mock import patch

import pytest

from src.gui.interface import Interface

# Configurar o ambiente para evitar que o Tkinter tente abrir janelas gráficas
os.environ["DISPLAY"] = ":99.0"  # Para sistemas macOS/Linux
os.environ["PYTHONUNBUFFERED"] = "1"


@pytest.fixture
def mock_interface():
    """Cria uma instância mock da interface p/ testes sem interface gráfica."""
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal para evitar interface gráfica

    with patch("tkinter.Tk", return_value=root), \
         patch("src.gui.livro_list.LivroList"), \
         patch("src.gui.livro_form.LivroForm"), \
         patch("src.managers.livro_manager.LivroManager"):
        interface = Interface()

    yield interface

    root.destroy()  # Fecha a interface ao final dos testes


def test_interface_inicializa_corretamente(mock_interface):
    """Testa se a interface inicializa corretamente."""
    assert mock_interface is not None


def test_componentes_instanciados(mock_interface):
    """Testa se os componentes principais foram criados corretamente."""
    assert hasattr(mock_interface, "livro_form")
    assert hasattr(mock_interface, "livro_list")
