g = 9.8 
function lancamento(v, yo, teta){

    var mult = v**2/(2*g);
    var raiz=  Math.sqrt(1+ (yo * g * 2)/(v**2 * Math.sin(teta)**2));
    var seno = Math.sin(2*teta);

    resultado = mult*(1+raiz)*seno;
    return resultado;

}

var v = lancamento(Math.sqrt(9.8), 1 , Math.PI/6)

console.log(resultado)
