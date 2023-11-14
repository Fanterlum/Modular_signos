import { View, Text, Button, TouchableOpacity, PixelRatio, Image} from 'react-native';
import React, { useState, useContext } from 'react';
import { DrawerActions } from '@react-navigation/routers';
import { StyleSheet } from 'react-native';
import { useNavigation } from '@react-navigation/native';
//se importa el chatbot
import ButtonChatbox from '../Chatbot/Components/ButtonChatbox';
//Log del usuario
import {useUser} from '../components/Context/UserProvider';
import { useEmail } from '../components/Context/EmailProvider';
//Info del usuario
import { useJson } from '../components/Context/JsonProvider';
const Dashboard = ({ navigation, route }) => {
  const { userID } = useUser();
  const { Email } = useEmail();
  const responsiveSize = PixelRatio.getPixelSizeForLayoutSize(10); // 50 DP
  //Tamaño de fotos
  const image1Height = PixelRatio.getPixelSizeForLayoutSize(50); // 50 DP
  const image1Width = PixelRatio.getPixelSizeForLayoutSize(129); // 50 DP

  //Fotos de los botones
  const patientBanner = require('../assets/PatientBanner2.jpg');
  const doctorBanner = require('../assets/DoctorBanner.jpg');
  const doctor2Banner = require('../assets/PatientListBanner.jpg');
  const [nombre, setNombre] = useState(''); // Variable para el nombre
  const [apellidos, setApellidos] = useState(''); // Variable para el apellido
  console.log(userID);
  console.log(Email);
  const {Json} = useJson();
  console.log(Json);
  
  let primerApellido = '';
  if (Json && Json.apellidos) {
    const apellidosArray = Json.apellidos.split(' '); // Divide la cadena de apellidos en un array

    if (apellidosArray.length > 0) {
      primerApellido = apellidosArray[0]; // Obtén el primer elemento del array como primer apellido
    }
  }
  //GetPatientof(cedula);
  const Dashboard = () =>{
    const navigation = useNavigation();
  }
  const openDrawer = () => {
    navigation.openDrawer();
  };
  return (
    <View style={styles.mainContainer}>
      <View style={styles.topContainer}>
        {Json ? (
          <Text style={[styles.title, { fontSize: responsiveSize }]}>
            Bienvenido {Json.username} {primerApellido}
          </Text>
        ) : (
          <Text style={[styles.title, { fontSize: responsiveSize }]}>Cargando...</Text>
        )}
      </View>
      <View style={styles.midContainer}>
        <TouchableOpacity
          style={styles.boton}
          onPress={() => {
            navigation.navigate('Paciente');
          }}
        >
          <Image source={patientBanner} style={[styles.BannerPatient, { height: image1Height, width: image1Width }]} />
          <Text style={[styles.buttonTitles, { left: "11%" }]}>Ver informacion sobre el paciente</Text>
        </TouchableOpacity>
        <TouchableOpacity
          style={styles.boton}
          onPress={() => {
            navigation.navigate('Doctor');
          }}
        >
          <Image source={doctorBanner} style={[styles.BannerPatient, { height: image1Height, width: image1Width }]} />
          <Text style={[styles.buttonTitles, { left: "14%" }]}>Ver informacion sobre el doctor</Text>
        </TouchableOpacity>
        <TouchableOpacity
          style={styles.boton}
          onPress={() => {
            navigation.navigate('Lista de pacientes');
          }}
        >
          <Image source={doctor2Banner} style={[styles.BannerPatient, { height: image1Height, width: image1Width }]} />
          <Text style={[styles.buttonTitles, { left: "25%" }]}>Ver lista de pacientes</Text>
        </TouchableOpacity>
      </View>
      <View style={styles.botContainer}>
        {/* botContainer se superpondrá sobre los demás elementos */}
        <View style={styles.buttonChatboxContainer}>
          {/* ButtonChatbox se posicionará en la mitad de la pantalla */}
          <ButtonChatbox></ButtonChatbox>
        </View>
      </View>
    </View>
  );
};

export default Dashboard

const styles = StyleSheet.create({
  buttonTitles: {
    position: 'absolute',
    top: "40%", // Ajusta la posición vertical del texto según tus necesidades
    fontSize: 18,
    color: 'white', // Ajusta el color del texto según tus necesidades
    fontWeight: "bold",
  },
  BannerPatient: {
    opacity: 0.5,
    borderRadius: 35,
  },
  boton:{
    backgroundColor: "black",
    width: "90%",
    margin: "2%",
    borderRadius: 35,
  },
  mainContainer:{
    width:"100%",
    height: "100%",
    flex:1,
  },
  topContainer:{
    width:"100%",
    height: "15%",
    backgroundColor: "white",
    justifyContent: 'center',
    alignItems: 'center',
  },
  midContainer:{
    width:"100%",
    height: "70%",
    backgroundColor: "white",
    justifyContent: 'center',
    alignItems: 'center',
  },
  botContainer: {
    position: 'absolute',
    bottom: 0,
    left: 0,
    right: 0,
    // Otros estilos para botContainer
  },
  buttonChatboxContainer: {
    position: 'absolute',
    bottom: '50%', // Coloca ButtonChatbox en la mitad de la pantalla
    left: 0,
    right: 0,
    // Otros estilos para el contenedor de ButtonChatbox si es necesario
  },
  title:{
    fontWeight: "bold",
  },
})