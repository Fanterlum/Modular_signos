import { StyleSheet, Text, View, Image, TouchableOpacity } from 'react-native';
import React, { useEffect, useState } from 'react';
import Bot_Photo from '../components/items/Bot_Photo';

//Asignador de color para el estado del paciente
import ColorAssigner from '../components/ColorAssigner';
import TextAssigner from '../components/TextAssigner';

//Los estilos del paciente
import { styles } from '../Styles/Patient-Doctor/styles'; // Ajusta la ruta según la ubicación del archivo
//Se importa el chatbot
import ButtonChatbox from "../Chatbot/Components/ButtonChatbox";
//Se importa la info del usuario
import GetInfo from '../backend/GetInfo';
//Info del doctor
import { useJson } from '../components/Context/JsonProvider';
//Navigation
import { useNavigation } from '@react-navigation/native'; // Importa la función useNavigation desde React Navigation

const Patient_ID_info = ({route}) => {
  const navigation = useNavigation(); // Obtiene el objeto de navegación
  const [nombre, setNombre] = useState("Cargando..."); // Variable para el nombre
  const [apellido, setApellido] = useState("Cargando..."); // Variable para el apellido
  const [edad, setEdad] = useState('22'); // Variable para la edad
  const userId = route.params?.userId;
  const {Json} = useJson();
  const [data, setData] = useState(null);
  //Aqui van los estados del paciente
  const [ActualState, setActualState] = useState(2); //ESTADO ACTUAL
  const [FutureState, setFutureStare] = useState(1); //Estado futuro

    useEffect(() => {
      const fetchDataWithId = async (id) => {
        try {
          // Llama a la función GetInfo para obtener datos basados en el ID
          const jsonData = await GetInfo(id);
          setNombre(jsonData.username);
          setApellido(jsonData.apellidos);
          if(jsonData.status>=0 && jsonData.status<=2){
            setActualState(jsonData.status);
            console.log("Entra");
          }
          // Puedes actualizar otras variables de estado según sea necesario
        } catch (error) {
          console.error('Error al obtener el JSON:', error);
        }
      };
      fetchDataWithId(userId);
    }, [userId]);

    let primerApellido = '';
    if (Json && Json.apellidos) {
      const apellidosArray = Json.apellidos.split(' '); // Divide la cadena de apellidos en un array
      if (apellidosArray.length > 0) {
        primerApellido = apellidosArray[0]; // Obtén el primer elemento del array como primer apellido
      }
    }

    const [Doctor, setDoctor] = useState(Json.username + " " + primerApellido); // Variable para la edad
    //Aqui va la ruta o la peticion a la imagen del paciente
    const imageUrl = require('../assets/Sample/Patient.jpeg');
    const navigateToStatistics = (userId) => {
      navigation.navigate('Estadistica', {userId: userId});
    };
    const navigateToHistory = () => {
      navigation.navigate('History');
    };
    return (
      <View style={styles.MainContainer}>
        <View style={styles.photoContainer}>
          <Text style={styles.titleText}>Datos del paciente:</Text>
          <Image source={imageUrl} style={styles.PatientPhoto}
                  resizeMode="contain" // Controla cómo se ajusta la imagen
                  />
        </View>
        <View style={styles.infoContainer}>
          <Text style={styles.DataText2}>Nombre: {nombre}</Text>
          <Text style={styles.DataText}>Apellido: {apellido}</Text>
          <Text style={styles.DataText}>Edad: {edad}</Text>
          <Text style={styles.DataText}>Doctor a cargo: {Doctor}</Text>
  
        </View>
        <View style={styles.Patient_StatusContainer}>
        <View style={[styles.estados, { backgroundColor: ColorAssigner({ numero: ActualState }) }]}>
          <Text style={styles.StatusText}>Status Actual: {TextAssigner({ numero: ActualState })}</Text>
        </View>
        <View style={[styles.estados, { backgroundColor: ColorAssigner({ numero: FutureState }) }]}>
          <Text style={styles.StatusText}>Status Futuro: {TextAssigner({ numero: FutureState })}</Text>
        </View>
        </View>
        <View style={styles.chatbotContainer}>
        <TouchableOpacity style={[styles.historial]} onPress={navigateToHistory}>
          <Text style={[styles.StatusText, {marginLeft: "10%",}]}>Historial Clinico</Text>
        </TouchableOpacity>
        <TouchableOpacity style={[styles.estadistica]} onPress={() => navigateToStatistics(userId)}>
          <Text style={[styles.StatusText, {marginLeft: "13%",}]}>Estadisticas</Text>
        </TouchableOpacity>
          <ButtonChatbox></ButtonChatbox>
        </View>
      </View>
      )
}

export default Patient_ID_info