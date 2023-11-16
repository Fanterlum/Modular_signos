import { View, Text, TouchableOpacity, PixelRatio } from 'react-native'
import React, { useState } from 'react';
import { StyleSheet } from 'react-native';
import { useNavigation } from '@react-navigation/native'; // Importa la función useNavigation desde React Navigation

//Asignador de color para el estado del paciente
import ColorAssigner from '../ColorAssigner';
import TextAssigner from '../TextAssigner';

const Patient_List_Item = ({paciente}) => {
  //Pixelratio para el contenedor principal
  const responsiveSize = PixelRatio.getPixelSizeForLayoutSize(16); // 50 DP
  const [nombre, setNombre] = useState(paciente.username); // Variable para el nombre
  const [apellido, setApellido] = useState(paciente.apellidos); // Variable para el apellido
  //Aqui van los estados del paciente
  const [ActualState, setActualState] = useState(2); //ESTADO ACTUAL paciente.estado
  if(paciente.status>=0 && paciente.status<=2){
    setActualState(paciente.status);
  }
  const navigation = useNavigation(); // Obtiene el objeto de navegación

  const handleViewDetails = (id) => {
    // Navega a la vista de detalles y pasa el ID como parámetro
    navigation.navigate('IdPaciente', { userId: id });
  };
  return (
    <View style={[styles.MainContainer,{height: responsiveSize}]}>
      <View style={[styles.State, { backgroundColor: ColorAssigner({ numero: ActualState }) }]}>
        <Text style={styles.StateText}>{TextAssigner({ numero: ActualState })}</Text>
      </View>
      <View style={styles.Name}>
        <Text style={styles.NameText}>{apellido} {nombre}</Text>
      </View>
      <TouchableOpacity style={styles.Action} onPress={() => handleViewDetails(paciente.id)}>
        <Text style={styles.ActionText}>Detalles</Text>
      </TouchableOpacity>
    </View>
  )
}

export default Patient_List_Item
const styles = StyleSheet.create({
    Action:{
        backgroundColor: "#75C3CC",
        height: "75%",
        width: "17%",
        marginTop: "2%",
        borderRadius: 25,
        alignContent: "center",
        justifyContent: "center",
    },
    ActionText: {
      color: "white",
      fontWeight: "bold",
      fontSize: 12,
      marginLeft: "2%",
    },
    Name: {
        backgroundColor: "white",
        width: "60%",
        height: "90%",
        marginTop: "1%",
        borderRadius: 25,
        borderColor: "white",
        borderWidth: 1,
    },
    NameText: {
        color: "black",
        fontWeight: "bold",
        fontSize: 12,
        marginLeft: "5%",
        marginTop: "5%",
    },
    State:{
        width: "20%",
        height: "90%",
        marginLeft: "2%",
        marginTop: "1%",
        borderRadius: 25,
        alignContent: "center",
        justifyContent: "center",
    },
    StateText: {
        color: "white",
        fontWeight: "bold",
        fontSize: 12,
        marginLeft: "10%",
    },
    MainContainer:{
        backgroundColor:"white",
        marginBottom: "2%",
        borderWidth: 1,
        borderRadius: 25,
        flexDirection: "row",
    },
});