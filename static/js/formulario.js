const form = document.getElementById("form-pedido");
const catalogo = JSON.parse(form.dataset.catalogo);

const selTipo = document.getElementById("tipo");
const selModelo = document.getElementById("modelo");
const selTamanho = document.getElementById("tamanho");
const listaItens = document.getElementById("lista-itens");
const avisoVazio = document.getElementById("vazio");
const campoItens = document.getElementById("itens");
const erro = document.getElementById("erro");

let itens = [];

function preencher(select, opcoes, textoInicial) {
    select.innerHTML = "";
    select.add(new Option(textoInicial, ""));
    for (const opcao of opcoes) {
        select.add(new Option(opcao, opcao));
    }
    select.disabled = opcoes.length === 0;
}

function limparEscolhas() {
    preencher(selTipo, Object.keys(catalogo), "Escolha o tipo");
    preencher(selModelo, [], "Escolha o modelo");
    preencher(selTamanho, [], "Escolha o tamanho");
}

function escolhaCompleta() {
    return Boolean(selTipo.value && selModelo.value && selTamanho.value);
}

function mostrarItens() {
    listaItens.innerHTML = "";
    itens.forEach((item, posicao) => {
        const linha = document.createElement("li");
        linha.textContent = `${item.modelo} (${item.tipo}) - tamanho ${item.tamanho}`;

        const botao = document.createElement("button");
        botao.type = "button";
        botao.textContent = "Remover";
        botao.addEventListener("click", () => {
            itens.splice(posicao, 1);
            mostrarItens();
        });

        linha.appendChild(botao);
        listaItens.appendChild(linha);
    });
    avisoVazio.hidden = itens.length > 0;
}

function adicionarItem() {
    itens.push({ tipo: selTipo.value, modelo: selModelo.value, tamanho: selTamanho.value });
    mostrarItens();
    limparEscolhas();
}

limparEscolhas();
mostrarItens();

selTipo.addEventListener("change", () => {
    const modelos = catalogo[selTipo.value] || {};
    preencher(selModelo, Object.keys(modelos), "Escolha o modelo");
    preencher(selTamanho, [], "Escolha o tamanho");
});

selModelo.addEventListener("change", () => {
    const modelos = catalogo[selTipo.value] || {};
    const tamanhos = modelos[selModelo.value] || [];
    preencher(selTamanho, tamanhos, "Escolha o tamanho");
});

document.getElementById("btn-adicionar").addEventListener("click", () => {
    if (!escolhaCompleta()) {
        erro.textContent = "Escolha tipo, modelo e tamanho antes de adicionar.";
        return;
    }
    erro.textContent = "";
    adicionarItem();
});

form.addEventListener("submit", (evento) => {
    if (escolhaCompleta()) {
        adicionarItem();
    }
    if (itens.length === 0) {
        evento.preventDefault();
        erro.textContent = "Adicione pelo menos um EPI à lista.";
        return;
    }
    erro.textContent = "";
    campoItens.value = JSON.stringify(itens);
});
