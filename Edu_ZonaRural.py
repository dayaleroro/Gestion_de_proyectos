# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# CONFIGURACIÓN DE LA PÁGINA
# -----------------------------
st.set_page_config(page_title="Proyecto Educación Rural con IA", page_icon="📊", layout="wide")

# -----------------------------
# ESTILOS CSS PERSONALIZADOS
# -----------------------------
st.markdown("""
    <style>
    .card {
        background-color: #f9f9f9;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        margin: 10px;
    }
    .card h3 {
        color: #2c3e50;
        font-size: 18px;
        margin-bottom: 10px;
    }
    .card p {
        font-size: 15px;
        color: #333;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------
# PORTADA
# -----------------------------
st.title("📊 Proyecto de Gestión de Proyectos")
st.subheader("Aplicación Educativa con Inteligencia Artificial en Zonas Rurales")
st.markdown("**Curso:** Gestión de Proyectos | **Autores:** [Tu Nombre Aquí]")

st.write("---")

# -----------------------------
# SECCIONES EN MENÚ LATERAL
# -----------------------------
menu = st.sidebar.radio("Ir a:",
    ["Introducción", "Objetivos", "Matriz del Proyecto", "Cronograma",
     "Costos", "Gestión", "EDT", "Diccionario EDT", "Matriz RACI", "Conclusiones"])

# -----------------------------
# SECCIONES
# -----------------------------
if menu == "Introducción":
    st.header("📌 Introducción")
    st.write("""
    La educación en zonas rurales enfrenta desafíos históricos: limitaciones en conectividad a internet,
    carencia de dispositivos tecnológicos, baja capacitación docente en herramientas digitales y desigualdades
    en el acceso al conocimiento.

    Frente a este panorama, el proyecto busca implementar una **plataforma educativa apoyada en Inteligencia Artificial (IA)**
    que permita a estudiantes y docentes de instituciones rurales acceder a análisis de datos educativos,
    personalización del aprendizaje y estrategias de enseñanza innovadoras.

    Este plan se fundamenta en una gestión estructurada con **cronograma, costos, aseguramiento de calidad y un plan de comunicación**,
    con el fin de garantizar sostenibilidad y efectividad en su implementación.
    """)

elif menu == "Objetivos":
    st.header("🎯 Objetivos")
    st.subheader("Objetivo General")
    st.write("""
    **Desarrollar e implementar una plataforma educativa con apoyo de Inteligencia Artificial (IA) que fortalezca
    la enseñanza y el aprendizaje en zonas rurales, superando las limitaciones de conectividad y acceso tecnológico.**
    """)

    st.subheader("Objetivos Específicos")
    st.write("""
    1. Diseñar e implementar un **cronograma estructurado** que contemple fases de diseño, desarrollo, piloto y despliegue, adaptado al contexto rural.
    2. Establecer **métricas e indicadores de calidad (KPIs)** para evaluar el impacto de la plataforma en los procesos de enseñanza-aprendizaje.
    3. Realizar un **plan de aseguramiento de calidad** mediante pruebas piloto en instituciones rurales, validando la usabilidad y pertinencia de la plataforma.
    4. Diseñar un **plan de gestión de personal** que incluya la capacitación docente en el uso de IA y herramientas digitales.
    5. Implementar una **estrategia de comunicación** que garantice el acompañamiento y la retroalimentación de los actores educativos (docentes, estudiantes, familias, entidades gubernamentales).
    6. Definir un esquema de **control de costos y sostenibilidad financiera** para asegurar la continuidad del proyecto más allá de la fase inicial de implementación.
    """)

elif menu == "Matriz del Proyecto":
    st.header("📋 Matriz del Proyecto")

    st.markdown(
        """
        <style>
        .stImage > img {
            width: 100% !important;
            height: auto !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.image("Educación Zona Rural.jpg", caption="Matriz de referencia del proyecto")

    st.write("A continuación, se muestra la matriz organizada en recuadros:")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('<div class="card"><h3>1. Cronograma</h3><p>Diseño (3 meses)<br>Desarrollo (6 meses)<br>Piloto (4 meses)<br>Despliegue (2 meses)</p></div>', unsafe_allow_html=True)
        st.markdown('<div class="card"><h3>6. Estimación de costos</h3><p>Presupuesto detallado con financiación de MinCiencias.</p></div>', unsafe_allow_html=True)
        st.markdown('<div class="card"><h3>12. Aseguramiento de calidad</h3><p>Pruebas de rendimiento y análisis de datos iniciales para validar usabilidad.</p></div>', unsafe_allow_html=True)
        st.markdown('<div class="card"><h3>18. Control de costos</h3><p>Seguimiento del presupuesto para evitar desviaciones.</p></div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card"><h3>7. Definición de métricas</h3><p>KPIs: Precisión del 90% y mejora del 15% en calificaciones.</p></div>', unsafe_allow_html=True)
        st.markdown('<div class="card"><h3>13. Adquisición del equipo</h3><p>Formación a docentes y administradores en el uso del dashboard.</p></div>', unsafe_allow_html=True)
        st.markdown('<div class="card"><h3>19. Control de calidad</h3><p>Monitoreo de KPIs y ajustes en los modelos de IA según resultados.</p></div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="card"><h3>8. Gestión de personal</h3><p>Definición de roles: ingeniero de datos, desarrollador, y necesidades de capacitación.</p></div>', unsafe_allow_html=True)
        st.markdown('<div class="card"><h3>9. Plan de comunicación</h3><p>Estrategia de reportes de avance y retroalimentación con stakeholders.</p></div>', unsafe_allow_html=True)

elif menu == "Cronograma":
    st.header("📅 Cronograma del Proyecto")

    data = {
        "Fase": ["Diseño", "Desarrollo", "Piloto", "Despliegue"],
        "Inicio": ["2025-01-01", "2025-04-01", "2025-10-01", "2026-02-01"],
        "Fin":    ["2025-03-31", "2025-09-30", "2026-01-31", "2026-03-31"]
    }
    df = pd.DataFrame(data)

    fig = px.timeline(
        df,
        x_start="Inicio",
        x_end="Fin",
        y="Fase",
        color="Fase",
        title="Cronograma del Proyecto",
        labels={"Fase": "Etapas"}
    )
    fig.update_yaxes(autorange="reversed")

    st.plotly_chart(fig, use_container_width=True)

    st.info("""
    👉 El cronograma contempla 4 fases principales:
    - **Diseño**: 3 meses
    - **Desarrollo**: 6 meses
    - **Piloto**: 4 meses
    - **Despliegue**: 2 meses
    """)

elif menu == "Costos":
    st.header("💰 Estimación y Control de Costos")
    st.write("""
    - Se gestionará financiamiento a través de convocatorias de **MinCiencias**.
    - Implementación de un plan de **control de costos** para evitar desviaciones.
    """)

elif menu == "Gestión":
    st.header("👥 Gestión del Proyecto")
    st.markdown('<div class="card"><h3>Gestión de personal</h3><p>Asignación de roles y capacitaciones.</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="card"><h3>Gestión de comunicación</h3><p>Canales de retroalimentación y reportes de avance.</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="card"><h3>Gestión de calidad</h3><p>Pruebas de rendimiento, KPIs y mejoras continuas.</p></div>', unsafe_allow_html=True)

# -------------------------------------------------------------------
# 🚀 NUEVA SECCIÓN 1: EDT
# -------------------------------------------------------------------
elif menu == "EDT":
    st.header("🧩 Estructura de Desglose del Trabajo (EDT)")
    st.subheader("Proyecto: Plataforma de Aprendizaje Adaptativo con IA para Zonas Rurales de Colombia")

    st.markdown("""
    ### 1. Iniciación
    #### 1.1 Acta de constitución del proyecto
    - 1.1.1 Análisis de viabilidad técnica y financiera  
    - 1.1.2 Definición de objetivos generales y específicos  
    - 1.1.3 Identificación de stakeholders clave (MEN, docentes, comunidades rurales)

    #### 1.2 Definición del alcance preliminar
    - 1.2.1 Identificación de requerimientos iniciales  
    - 1.2.2 Priorización de entregables iniciales  
    - 1.2.3 Aprobación del alcance del piloto

    ---

    ### 2. Planificación
    #### 2.1 Plan de gestión del alcance
    - 2.1.1 Requerimientos funcionales de la plataforma  
    - 2.1.2 Diseño del modelo de recomendación y analítica de aprendizaje  
    - 2.1.3 Elaboración de matriz de trazabilidad de requisitos

    #### 2.2 Plan de gestión del tiempo
    - 2.2.1 Elaboración del cronograma (Diseño, Desarrollo, Piloto, Despliegue)  
    - 2.2.2 Estimación de duración y recursos de cada fase  
    - 2.2.3 Validación del cronograma con stakeholders

    #### 2.3 Plan de gestión de costos
    - 2.3.1 Presupuesto detallado del proyecto  
    - 2.3.2 Identificación de fuentes de financiación (Gobierno Nacional / Minciencias)  
    - 2.3.3 Estimación de costos por fase

    #### 2.4 Plan de gestión de calidad
    - 2.4.1 Definición de métricas e indicadores de desempeño (KPIs)  
    - 2.4.2 Establecimiento de criterios de aceptación de entregables  
    - 2.4.3 Elaboración del plan de aseguramiento de calidad

    #### 2.5 Plan de gestión de recursos humanos
    - 2.5.1 Definición de roles (ingeniero de datos, diseñador instruccional, docente líder)  
    - 2.5.2 Identificación de necesidades de capacitación  
    - 2.5.3 Asignación de responsabilidades

    #### 2.6 Plan de gestión de comunicaciones
    - 2.6.1 Estrategia de comunicación con los stakeholders  
    - 2.6.2 Definición de canales y frecuencia de reporte  
    - 2.6.3 Plan de reuniones y retroalimentación

    #### 2.7 Plan de gestión de riesgos
    - 2.7.1 Identificación y categorización de riesgos  
    - 2.7.2 Plan de mitigación (problemas de conectividad, hardware, sincronización)  
    - 2.7.3 Estrategia de contingencia

    #### 2.8 Plan de adquisiciones
    - 2.8.1 Identificación de bienes y servicios requeridos (tablets, routers, software IA)  
    - 2.8.2 Selección de proveedores  
    - 2.8.3 Elaboración del cronograma de compras

    ---

    ### 3. Ejecución
    #### 3.1 Dirección y gestión del desarrollo de la plataforma
    - 3.1.1 Coordinación del equipo de trabajo  
    - 3.1.2 Desarrollo del backend, modelo IA y dashboards  
    - 3.1.3 Integración de datos educativos rurales

    #### 3.2 Ejecución del plan de capacitación
    - 3.2.1 Formación docente en uso de herramientas digitales  
    - 3.2.2 Talleres de apropiación tecnológica  
    - 3.2.3 Entrenamiento en interpretación de métricas

    #### 3.3 Implementación piloto
    - 3.3.1 Instalación de equipos y software  
    - 3.3.2 Pruebas funcionales en 5 instituciones rurales  
    - 3.3.3 Ajustes según retroalimentación

    #### 3.4 Gestión de comunicaciones y acompañamiento
    - 3.4.1 Difusión de avances del proyecto  
    - 3.4.2 Reportes de progreso a stakeholders  
    - 3.4.3 Evaluación de satisfacción de usuarios

    ---

    ### 4. Control y Seguimiento
    #### 4.1 Monitoreo y control del alcance
    - 4.1.1 Revisión de entregables completados  
    - 4.1.2 Validación de cumplimiento de objetivos

    #### 4.2 Control de calidad
    - 4.2.1 Ejecución de pruebas de rendimiento y usabilidad  
    - 4.2.2 Análisis de resultados de las métricas  
    - 4.2.3 Emisión de informes de aseguramiento

    #### 4.3 Control de costos y presupuesto
    - 4.3.1 Seguimiento de ejecución financiera  
    - 4.3.2 Identificación de desviaciones y ajustes

    #### 4.4 Control de riesgos
    - 4.4.1 Seguimiento a la mitigación de riesgos  
    - 4.4.2 Evaluación del impacto de los riesgos residuales

    ---

    ### 5. Cierre
    #### 5.1 Cierre de adquisiciones
    - 5.1.1 Finalización de contratos con proveedores  
    - 5.1.2 Verificación de cumplimiento contractual

    #### 5.2 Cierre administrativo y técnico
    - 5.2.1 Presentación de informe final al MEN  
    - 5.2.2 Documentación de lecciones aprendidas  
    - 5.2.3 Entrega de productos y manuales finales

    #### 5.3 Plan de transición y sostenibilidad
    - 5.3.1 Preparación del plan de sostenibilidad a largo plazo  
    - 5.3.2 Propuesta de escalabilidad del proyecto a otras zonas rurales
    """)

# -------------------------------------------------------------------
# 🚀 NUEVA SECCIÓN 2: Diccionario EDT
# -------------------------------------------------------------------
elif menu == "Diccionario EDT":
    st.header("📘 Diccionario de la EDT")
    st.subheader("Proyecto: Plataforma de Aprendizaje Adaptativo con Inteligencia Artificial para Zonas Rurales de Colombia")

    st.markdown("""
    ### 1. Iniciación
    **1.1 Acta de constitución del proyecto**  
    Formaliza el inicio del proyecto y define los objetivos generales, el alcance preliminar y las fuentes de financiación.  
    **Responsable:** Director del proyecto  
    **Criterio de aceptación:** Documento aprobado por el comité directivo y el MEN  

    **1.2 Definición del alcance preliminar**  
    Describe los límites del proyecto, los entregables y las instituciones beneficiadas.  
    **Responsable:** Gestor de alcance  
    **Criterio de aceptación:** Documento validado por las instituciones participantes  

    ---

    ### 2. Planificación
    **2.1 Plan de gestión del alcance**  
    Define los requerimientos funcionales y los criterios de aceptación de cada módulo de IA.  
    **Responsable:** Ingeniero de requerimientos  
    **Criterio de aceptación:** Documento revisado y aprobado por el comité técnico  

    **2.2 Plan de gestión del tiempo**  
    Incluye el cronograma detallado con fases de diseño, desarrollo, piloto y despliegue.  
    **Responsable:** Líder de planeación  
    **Criterio de aceptación:** Cronograma validado por el equipo  

    **2.3 Plan de gestión de costos**  
    Contiene la estimación presupuestal y fuentes de financiación.  
    **Responsable:** Analista financiero  
    **Criterio de aceptación:** Presupuesto aprobado por los entes financiadores  

    **2.4 Plan de gestión de calidad**  
    Define indicadores de desempeño (KPIs) y plan de aseguramiento de calidad.  
    **Responsable:** Coordinador de calidad  
    **Criterio de aceptación:** Documento alineado con estándares institucionales  

    **2.5 Plan de gestión de recursos humanos**  
    Establece roles y responsabilidades del equipo, y necesidades de capacitación.  
    **Responsable:** Coordinador de recursos humanos  
    **Criterio de aceptación:** Plan aprobado y comunicado al equipo  

    **2.6 Plan de gestión de comunicaciones**  
    Detalla mecanismos y canales de comunicación entre los actores.  
    **Responsable:** Gestor de comunicaciones  
    **Criterio de aceptación:** Cronograma validado con las partes interesadas  

    **2.7 Plan de gestión de riesgos**  
    Analiza riesgos tecnológicos, financieros y operativos.  
    **Responsable:** Coordinador de riesgos  
    **Criterio de aceptación:** Plan aprobado por la dirección  

    **2.8 Plan de adquisiciones**  
    Describe los bienes y servicios requeridos, proveedores y tiempos de entrega.  
    **Responsable:** Gestor de compras  
    **Criterio de aceptación:** Plan firmado por dirección y proveedores  

    ---

    ### 3. Ejecución
    **3.1 Dirección y gestión del desarrollo de la plataforma**  
    Coordina el desarrollo técnico, la IA y el dashboard educativo.  
    **Responsable:** Líder técnico  
    **Criterio de aceptación:** Versiones probadas y validadas  

    **3.2 Ejecución del plan de capacitación**  
    Formación docente y talleres de apropiación tecnológica.  
    **Responsable:** Coordinador pedagógico  
    **Criterio de aceptación:** Evidencias y reportes de asistencia  

    **3.3 Implementación piloto**  
    Prueba de la plataforma en instituciones rurales.  
    **Responsable:** Gestor de implementación  
    **Criterio de aceptación:** Informe de resultados y ajustes realizados  

    **3.4 Gestión de comunicaciones y acompañamiento**  
    Difusión de avances y reportes de progreso.  
    **Responsable:** Gestor de comunicaciones  
    **Criterio de aceptación:** Reportes aprobados  

    ---

    ### 4. Control y Seguimiento
    **4.1 Monitoreo y control del alcance**  
    Revisión del cumplimiento de objetivos y entregables.  
    **Responsable:** Gestor de control  
    **Criterio de aceptación:** Informes validados  

    **4.2 Control de calidad**  
    Pruebas de rendimiento y análisis de métricas.  
    **Responsable:** Coordinador de calidad  
    **Criterio de aceptación:** Cumplimiento de KPIs  

    **4.3 Control de costos y presupuesto**  
    Seguimiento financiero y ajustes.  
    **Responsable:** Analista financiero  
    **Criterio de aceptación:** Reporte actualizado  

    **4.4 Control de riesgos**  
    Monitoreo y mitigación continua de riesgos.  
    **Responsable:** Coordinador de riesgos  
    **Criterio de aceptación:** Registro actualizado  

    ---

    ### 5. Cierre
    **5.1 Cierre de adquisiciones**  
    Finalización de contratos y verificación de cumplimiento.  
    **Responsable:** Gestor de compras  
    **Criterio de aceptación:** Actas firmadas  

    **5.2 Cierre administrativo y técnico**  
    Entrega del informe final y documentación de lecciones aprendidas.  
    **Responsable:** Director del proyecto  
    **Criterio de aceptación:** Informe validado por la entidad  

    **5.3 Plan de transición y sostenibilidad**  
    Estrategia para continuidad y expansión del proyecto.  
    **Responsable:** Director de sostenibilidad  
    **Criterio de aceptación:** Plan aprobado por las instituciones
    """)

# -------------------------------------------------------------------
# 🚀 NUEVA SECCIÓN 3: Matriz RACI
# -------------------------------------------------------------------
elif menu == "Matriz RACI":
    st.title("📊 Matriz RACI – Proyecto: Plataforma de Aprendizaje Adaptativo con IA en Zonas Rurales")

    st.markdown("""
    La matriz **RACI** permite identificar los **roles y responsabilidades** de los miembros del proyecto en cada actividad clave del **EDT**.

    - **R (Responsable):** ejecuta la actividad.  
    - **A (Aprobador):** valida o aprueba el resultado.  
    - **C (Consultado):** brinda asesoría o información.  
    - **I (Informado):** recibe comunicación del avance.

    ---
    """)

    
    
  # --- Datos de la matriz RACI ---
data = {
    "Actividad / Tarea": [
        "1.1 Acta de constitución del proyecto",
        "1.2 Definición del alcance preliminar",
        "2.1 Plan de gestión del alcance",
        "2.2 Plan de gestión del cronograma",
        "2.3 Plan de gestión de costos",
        "2.4 Plan de gestión de calidad",
        "2.5 Plan de gestión de recursos humanos",
        "2.6 Plan de comunicaciones",
        "2.7 Plan de gestión de riesgos",
        "3.1 Diseño de la arquitectura de la plataforma",
        "3.2 Desarrollo del módulo de IA",
        "3.3 Integración de la base de datos y servidor",
        "3.4 Pruebas de funcionalidad",
        "3.5 Implementación del sistema piloto",
        "3.6 Capacitación docente y técnica",
        "4.1 Seguimiento al cronograma y costos",
        "4.2 Control de calidad del producto",
        "4.3 Gestión de incidencias y cambios",
        "5.1 Evaluación del impacto del proyecto",
        "5.2 Entrega final y documentación",
        "5.3 Cierre administrativo y lecciones aprendidas"
    ],
    "Director del Proyecto": [
        "A", "A", "A", "A", "A", "A", "I", "A", "A",
        "I", "I", "A", "I", "A", "I", "A", "A", "A", "A", "A", "A"
    ],
    "Gestor de Alcance": [
        "C", "R", "R", "I", "I", "I", "I", "I", "I",
        "I", "I", "I", "I", "I", "I", "I", "I", "I", "C", "I", "I"
    ],
    "Ingeniero de Requerimientos": [
        "I", "C", "C", "I", "I", "I", "I", "I", "I",
        "R", "C", "C", "I", "I", "I", "I", "I", "I", "I", "I", "I"
    ],
    "Desarrollador de Software": [
        "I", "I", "I", "C", "C", "I", "I", "I", "I",
        "C", "R", "R", "R", "C", "I", "I", "I", "C", "I", "I", "I"
    ],
    "Especialista en IA": [
        "I", "I", "C", "I", "I", "I", "I", "I", "C",
        "C", "R", "C", "C", "C", "I", "I", "I", "C", "I", "I", "I"
    ],
    "Administrador de Base de Datos": [
        "I", "I", "I", "I", "C", "I", "I", "I", "I",
        "C", "C", "R", "C", "I", "I", "I", "I", "I", "I", "I", "I"
    ],
    "Coordinador de Calidad": [
        "I", "I", "I", "I", "I", "R", "I", "I", "I",
        "I", "I", "I", "R", "I", "I", "I", "R", "I", "I", "I", "I"
    ],
    "Docente Líder": [
        "I", "C", "I", "I", "I", "C", "I", "I", "I",
        "I", "I", "I", "C", "R", "R", "I", "C", "I", "C", "C", "I"
    ],
    "Gestor de Comunicaciones": [
        "I", "I", "I", "I", "I", "I", "I", "R", "I",
        "I", "I", "I", "I", "I", "C", "I", "I", "I", "I", "I", "I"
    ],
    "Analista Financiero": [
        "I", "I", "I", "C", "R", "I", "I", "I", "I",
        "I", "I", "I", "I", "I", "I", "R", "I", "I", "I", "I", "I"
    ],
    "Stakeholders / MEN": [
        "I", "I", "I", "I", "I", "I", "I", "I", "I",
        "I", "I", "I", "I", "I", "I", "I", "I", "I", "A", "A", "I"
    ]
}

df_raci = pd.DataFrame(data)
st.dataframe(df_raci, use_container_width=True)
  
                                    
