import { StyleSheet, Text, View, Image, TouchableOpacity } from 'react-native';
import React, { useState } from 'react';
import Bot_Photo from '../components/items/Bot_Photo';

//Asignador de color para el estado del paciente
import ColorAssigner from '../components/ColorAssigner';
import TextAssigner from '../components/TextAssigner';

//Los estilos del paciente
import { styles } from '../Styles/Patient-Doctor/styles'; // Ajusta la ruta según la ubicación del archivo

//Import al chatbot
import ButtonChatbox from '../Chatbot/Components/ButtonChatbox';
/*
  Requerimientos al backend
  Si es un paciente el que ingresa, obtener el doctor que esta a su cargo por id
  y mostrar ese los datos del doctor
  en el caso de ser doctor, simplemente mostrarle su info
*/
const Doctor_Info = () => {
  const [nombre, setNombre] = useState('Vicente'); // Variable para el nombre
  const [apellido, setApellido] = useState('González Garcia'); // Variable para el apellido
  const [cedula, setCedula] = useState('218694551'); // Variable para la edad
  const [especialidad, setEspecialidad] = useState('Neumologo');
  //Aqui van los estados del paciente
  const [ActualState, setActualState] = useState(0); //ESTADO ACTUAL
  const [FutureState, setFutureStare] = useState(1); //Estado futuro

  //Aqui va la ruta o la peticion a la imagen del paciente
  const doctorPhoto = require('../assets/Sample/Doctor.jpeg');
  const handlePress = () => {
    // Manejar la acción cuando se presiona el botón
    console.log('El botón fue presionado');
  };

  return (
    <View style={styles.MainContainer}>
      <View style={styles.photoContainer}>
        <Text style={styles.titleText}>Datos del doctor:</Text>
        <Image source={doctorPhoto} style={styles.PatientPhoto}
                resizeMode="contain" // Controla cómo se ajusta la imagen
                />
      </View>
      <View style={styles.infoContainer}>
        <Text style={styles.DataText2}>Nombre: {nombre}</Text>
        <Text style={styles.DataText}>Apellido: {apellido}</Text>
        <Text style={styles.DataText}>Especialidad: {especialidad}</Text>
        <Text style={styles.DataText}>Cédula profesional: {cedula}</Text>
      </View>
      <View style={styles.Patient_StatusContainer}>
      </View>
      <View style={styles.botContainer}>
        {/* botContainer se superpondrá sobre los demás elementos */}
        <View style={styles.buttonChatboxContainer}>
          {/* ButtonChatbox se posicionará en la mitad de la pantalla */}
          <ButtonChatbox></ButtonChatbox>
        </View>
      </View>
    </View>
  )
}

export default Doctor_Info