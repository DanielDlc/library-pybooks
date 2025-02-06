from unittest.mock import MagicMock, patch

import pytest

from src.gui.interface import Interface


@pytest.fixture
def mock_interface():
    """Mock da interface para testes sem exibição gráfica."""
    with patch("tkinter.Tk"), \
         patch("src.gui.livro_list.LivroList"), \
         patch("src.gui.livro_form.LivroForm"), \
         patch("src.managers.livro_manager.LivroManager"):
        return Interface()


def test_interface_inicializa_corretamente(mock_interface):
    """Verifica se a interface inicializa sem erros."""
    assert isinstance(mock_interface, Interface)
    assert isinstance(mock_interface.janela, MagicMock)


def test_componentes_instanciados(mock_interface):
    """Verifica se os componentes da interface são criados corretamente."""
    assert hasattr(mock_interface, "livro_list")
    assert hasattr(mock_interface, "livro_form")
    assert hasattr(mock_interface, "livro_manager")
