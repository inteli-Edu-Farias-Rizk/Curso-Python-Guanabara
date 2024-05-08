function vetor(lista){
    var cont = 0;
    var iguais = [];
    while (cont < lista.length){
        if(lista[cont] === cont){
            iguais.push(cont);
        }
        cont++;
    };
    return iguais;
}

var k = vetor([0,1,2,3,4]);

console.log(k);

