¿Qué hace el bloque try/except ValueError? ¿Qué pasaría si el usuario escribe “veinte” y quitamos ese bloque?

Diccionarios y funciones (los refranes)
4. ¿Por qué guardamos los refranes en un diccionario y no en una lista? ¿Qué ventaja tiene que el refrán sea la clave y el significado el valor?
R: yo creo porque de esta forma de peden generar 'parejas' cada refran con su explicacion

5. ¿Para qué sirven las funciones decir_refran() y decir_refran_especifico()? ¿En qué se diferencian?
R: el primero es aleatorio y el segundo un especifico


6. Si quisieras agregar un refrán de tu propia abuela, ¿qué línea tendrías que modificar? ¿Hay que cambiar algo más?
R:  el reframes. solamente

Decisiones (if / elif / else)

7. En el programa, ¿qué refrán recibe una persona de 18 años? ¿Y una de 17? Explica por qué.
R: "Uno pone y Dios dispone.", la de 17, "Agua que no has de beber, dejala correr."

8. ¿Qué pasaría si cambiáramos el orden y pusiéramos primero if edad >= 18 y después elif edad >= 60? ¿Alguien recibiría alguna vez el refrán de “Agua que no has de beber”?
R: “Agua que no has de beber” no se mostraría jamás.

API y JSON (Parte 2)
9. ¿Qué convierte json.loads() y en qué se transforma? ¿Y json.dumps(), qué hace en dirección contraria?
R: pasa del textp al JSON y se convierte en diccionario tal vez? El dumps hace exactamente lo contrario. 

10. Para obtener la ciudad del usuario, escribimos datos['address']['city']. ¿Por qué necesitamos dos pares de corchetes?
R: proque son dos diccionariso

11. Hay tres tipos de error en esa parte (HTTPError, URLError y JSONDecodeError). ¿Cuál ocurriría si no tienes internet? ¿Y si el servidor responde con una página rota?
R: URLError no se pudo conectar, HTTPError contesta el servidor ero hay un eror. JSONDecodeError malo malo... viene corrupto quizas. 

12. ¿Por qué es buena idea usar timeout=10 al hacer la petición?
R: de lo contrario el programa podria quedarse pegado para siempre, con 10 segundos, lo cortas. 

Juego y reflexión general (Parte 3)
13. En el juego “Completa el refrán”, ¿cómo divide el programa el refrán en dos mitades? ¿Qué hacen split(), join() y //?
R: //2  y el split corta el refram e lsita de palabras. 

14. ¿Para qué sirve el bloque if __name__ == "__main__": al final del archivo?
R: esto hace que el programa corra o se ejecute y este al archivo presente, no funciona si el archivo es importado. 

15. Pregunta abierta: si tuvieras que agregar una cuarta parte al programa, ¿qué agregarías y qué conceptos nuevos necesitarías usar?
R: quizas poner un puntaje en el juego o un buscador. 