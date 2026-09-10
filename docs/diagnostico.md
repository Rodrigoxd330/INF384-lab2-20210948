
1.1 **Los defectos**: 
    1. El job 'publicación' se da a pesar de que el job 'validar' de error. Esto tiene como consecuencia que la validacion (quality gate) no esté funcionando correctamente.
    2. Las dependencias se instalan desde el archivo 'requirements.txt', el cual debe actualizarse siempre que se agregue una dependencia. Esto puede inducir a tener problemas de dependencias.
    3. Cualquier push a cualquier rama ejecuta el pipeline lo que haría que se repitan validaciones siempre. Esto significa que el pipelina se ejeuctará más veces innecesariamente.
    4. Se descarga el código desde el inicio (fetch: 0) se revisan los cambios desde el inicio. En la descarga del código, innecesariamente se descarga todo.

1.2 **Defecto de mayor duración**: Se aprecia como un defecto que demora tanto en 'validar' como en 'publicar' es la instalación de dependencias, se ve que dura 6-8 segundos en ambos. Se pudo ver gracias a que al ver el detalle de las actions, se muestra cuando demora cada step
1.3 **Vínculo con el caso**: Si l
1.4 **La métrica DORA**: La métrica DORA que esperaría mover sería el lead time para cambios y podría verse en que el pipeline se demorará menos en ejecutarse (se podría ver en el historial de actions)
1.5 **Proxy**: Tiempo de ejecución del pipeline


4.1 Medición posterior: 

4.2 Justificación de la versión: Solo el tercer punto de la versión pues solo se realizaron fixes

4.3 

4.4 Uso de IA: Se utilizó exclusivamente para la sintaxis de cachear las dependencia y para saber como sacar el nombre de la versión desde el yaml.     