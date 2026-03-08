# Bootcamp Python - SESIÓN 3

## 3. NOMBRES DE  VARIABLES / CONSTANTES

* Es la manera de identificar una variable o constante en el código.

* Seguiremos unas convenciones de nombres para los nombres de variables y constantes.

* Daremos los siguientes pasos para asignar correctamente los nombres:
    1. Reglas y convenciones de nombres.
    2. Nombres válidos.
    3. Nombres no válidos.

## NOMBRES DE VARIABLES / CONSTANTES - REGLAS Y CONVENCIONES

**COMBINACIÓN DE:**

* Letras MAYUSCULAS (A-Z) y minúsculas (a-z).
* Números (0-9).
* Guiones bajos (_).

**REGLAS Y CONVENCIONES:**

* No se pueden usar espacios en blanco.
* No se pueden usar caracteres especiales (%, $, &, etc.).
* No se pueden usar palabras reservadas del lenguaje (if, else, while, for, etc.).
* No se pueden comenzar con un número.
* Sensibles a mayúsculas y minúsculas (edad, Edad y EDAD son diferentes).
* Usar nombres descriptivos y significativos (edad, nombre_usuario, etc.).
* Usar notación camelCase o snake_case para nombres compuestos (nombreUsuario o nombre_usuario).
* Evitar el uso de abreviaturas o acrónimos poco comunes.
* Usar nombres en inglés para mayor compatibilidad internacional (age, user_name, etc.).
* Constantes en mayúsculas con guiones bajos (PI, MAX_VALUE, etc.).
* Evitar el uso de letras individuales a menos que sea en contextos específicos (i, j para índices).
* Mantener la longitud del nombre razonable (ni demasiado corto ni demasiado largo).
* Seguir las convenciones de estilo del proyecto o equipo.
* Documentar el propósito de variables y constantes complejas con comentarios.
* Revisar y refactorizar nombres según sea necesario para mejorar la claridad del código.
* Usar prefijos o sufijos para indicar el tipo de dato si es relevante (str_name, int_age, etc.).
* Evitar el uso de nombres que puedan causar confusión con funciones o métodos existentes.
* Considerar el contexto y ámbito de la variable o constante al nombrarla (global, local, etc.).
* Usar nombres que reflejen la unidad de medida si es aplicable (speed_kmh, weight_kg, etc.).
* Evitar el uso de nombres que puedan ser ofensivos o inapropiados en cualquier cultura.
* Mantener la coherencia en el estilo de nombres a lo largo de todo el proyecto.
* Revisar las mejores prácticas y convenciones de la comunidad para el lenguaje específico que se está utilizando.
* Usar nombres que faciliten la comprensión del código para otros desarrolladores.
* Evitar el uso de nombres que puedan ser confundidos con palabras clave del lenguaje.
* Considerar el uso de nombres que reflejen el estado o la función de la variable o constante (is_active, has_permission, etc.).
* Usar nombres que sean fáciles de recordar y escribir.
* Evitar el uso de nombres que puedan ser ambiguos o tener múltiples interpretaciones.
* Mantener un equilibrio entre la claridad y la concisión en los nombres.
* Revisar y actualizar los nombres según sea necesario a medida que el código evoluciona.
* Usar nombres que reflejen el contexto del proyecto o dominio específico (user_profile, order_details, etc.).
* Evitar el uso de nombres que puedan ser confundidos con otros elementos del código (variables, funciones, clases, etc.).
* Considerar el uso de nombres que reflejen la temporalidad o duración si es relevante (temp_data, session_timeout, etc.).
* Usar nombres que faciliten la depuración y el mantenimiento del código.
* Evitar el uso de nombres que puedan ser confundidos con convenciones de otros lenguajes de programación.
* Mantener un estilo de nombres consistente con las bibliotecas o frameworks utilizados en el proyecto.
* Revisar y adaptar los nombres según las necesidades específicas del proyecto o equipo de desarrollo.
* Usar nombres que reflejen la jerarquía o estructura del código si es relevante (parent_child, module_submodule, etc.).
* Evitar el uso de nombres que puedan ser confundidos con términos técnicos o jerga específica del dominio.
* Considerar el uso de nombres que reflejen la frecuencia de uso si es relevante (frequent_user, rare_event, etc.).
* Usar nombres que faciliten la colaboración y el trabajo en equipo.
* Evitar el uso de nombres que puedan ser confundidos con convenciones de estilo populares (kebab-case, PascalCase, etc.).
* Mantener un enfoque centrado en la legibilidad y comprensión del código al nombrar variables y constantes.
* Revisar y actualizar los nombres según las mejores prácticas y estándares de la industria.
* Usar nombres que reflejen la intención y propósito de la variable o constante en el contexto del proyecto.
* Evitar el uso de nombres que puedan ser confundidos con términos coloquiales o jerga popular.
* Considerar el uso de nombres que reflejen la modularidad o encapsulamiento si es relevante (module_var, encapsulated_data, etc.).
* Usar nombres que faciliten la integración con otras partes del código o sistemas externos.
* Evitar el uso de nombres que puedan ser confundidos con convenciones de nomenclatura de bases de datos (camelCase vs snake_case).
* Mantener un enfoque coherente y sistemático al nombrar variables y constantes en todo el proyecto.
* Revisar y adaptar los nombres según las necesidades cambiantes del proyecto o equipo de desarrollo.
* Usar nombres que reflejen la escalabilidad o flexibilidad si es relevante (scalable_system, flexible_config, etc.).
* Evitar el uso de nombres que puedan ser confundidos con términos técnicos específicos de otros dominios (networking, database, etc.).
* Considerar el uso de nombres que reflejen la seguridad o privacidad si es relevante (secure_data, private_info, etc.).
* Usar nombres que faciliten la documentación y el seguimiento del código.
* Evitar el uso de nombres que puedan ser confundidos con convenciones de estilo de otros lenguajes de programación (snake_case vs camelCase).
* Mantener un enfoque centrado en la claridad y precisión al nombrar variables y constantes.
* Revisar y actualizar los nombres según las mejores prácticas y estándares de la comunidad de desarrollo.
* Usar nombres que reflejen la interoperabilidad o compatibilidad si es relevante (cross_platform, compatible_format, etc.).
* Evitar el uso de nombres que puedan ser confundidos con términos técnicos específicos de otros lenguajes de programación (Java, C++, etc.).
* Considerar el uso de nombres que reflejen la eficiencia o rendimiento si es relevante (fast_algorithm, optimized_code, etc.).
* Usar nombres que faciliten la colaboración entre diferentes equipos o departamentos.
* Evitar el uso de nombres que puedan ser confundidos con convenciones de estilo de otros lenguajes de programación (PascalCase vs kebab-case).
* Mantener un enfoque coherente y sistemático al nombrar variables y constantes en todo el proyecto.
* Revisar y adaptar los nombres según las necesidades cambiantes del proyecto o equipo de desarrollo.
* Usar nombres que reflejen la sostenibilidad o mantenibilidad si es relevante (maintainable_code, sustainable_design, etc.).
* Evitar el uso de nombres que puedan ser confundidos con términos técnicos específicos de otros dominios (AI, ML, etc.).
* Considerar el uso de nombres que reflejen la innovación o creatividad si es relevante (innovative_solution, creative_approach, etc.).
* Usar nombres que faciliten la comprensión y el aprendizaje para nuevos desarrolladores.
* Evitar el uso de nombres que puedan ser confundidos con convenciones de estilo de otros lenguajes de programación (snake_case vs PascalCase).
* Mantener un enfoque centrado en la claridad y precisión al nombrar variables y constantes.
* Revisar y actualizar los nombres según las mejores prácticas y estándares de la comunidad de desarrollo.
* Usar nombres que reflejen la adaptabilidad o flexibilidad si es relevante (adaptable_system, flexible_design, etc.).
* Evitar el uso de nombres que puedan ser confundidos con términos técnicos específicos de otros dominios (cloud, IoT, etc.).
* Considerar el uso de nombres que reflejen la colaboración o trabajo en equipo si es relevante (team_project, collaborative_tool, etc.).
* Usar nombres que faciliten la integración con otras partes del código o sistemas externos.
* Evitar el uso de nombres que puedan ser confundidos con convenciones de nomenclatura de bases de datos (camelCase vs snake_case).

### **ESAS SON ALGUNAS RECOMENDACIONES PARA NOMBRAR VARIABLES Y CONSTANTES**

**PARA MAS INFORMACIÓN CONSULTAR EL MANUAL DE DISEÑO PEP 8 DE PYTHON:** <https://peps.python.org/pep-0008/#naming-conventions>
