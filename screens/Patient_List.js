import { FlatList, View, Text, Button, TouchableOpacity, Image} from 'react-native';
import React, {useEffect} from 'react';
import { StyleSheet } from 'react-native';
import { useFocusEffect } from '@react-navigation/native';


//Backend
import GetPatientof from '../backend/GetPatientof';
//Json del usuario
import { useJson } from '../components/Context/JsonProvider';
//Componente de cada paciente mostrado
import Patient_List_Item from '../components/items/Patient_List_Item';
//Se settea la lista
import { useList } from "../components/Context/PatientList";

//Importamos el chatbot
import ButtonChatbox from '../Chatbot/Components/ButtonChatbox';
/*
  Requerimientos al backend
  Se hace una consulta a todos los pacientes de x doctor
  Se buscan en la tabla de pacientes por el ID de doctor a cargo
  y devuelven una constante con todos los datos
  Se muestran de mayor a menor urgencia
*/
const Patient_List = () => {
  const {Json} = useJson();
  const {setList} = useList();
  //console.log(Json);
  useFocusEffect(
    React.useCallback(() => {
    // Llamar a getUserInfo cuando el componente se monte
    const cedula = '2';
     // Reemplaza con el ID de usuario adecuado
    getPatientsInfo(cedula);
    }, [])
  );
  const getPatientsInfo = async (cedula) => {
    try {
      const pacientes = await GetPatientof({cedula: cedula});
      setList(pacientes);
    } catch (error) {
      console.error("Error al obtener la información del usuario:", error);
    }
  };
  const {List} = useList();
  console.log(List);
  /*
  const pacientes = [
    { id: 1, nombre: 'Juan', apellido: 'Pérez', estado: 0 }, // Grave
    { id: 2, nombre: 'María', apellido: 'Gómez', estado: 1 }, // Inestable
    { id: 3, nombre: 'Luis', apellido: 'González', estado: 2 }, // Estable
    { id: 4, nombre: 'Ana', apellido: 'Martínez', estado: 0 }, // Grave
    { id: 5, nombre: 'Pedro', apellido: 'López', estado: 1 }, // Inestable
    { id: 6, nombre: 'Laura', apellido: 'Rodríguez', estado: 2 }, // Estable
    { id: 7, nombre: 'Carlos', apellido: 'Fernández', estado: 0 }, // Grave
    { id: 8, nombre: 'Sofía', apellido: 'Díaz', estado: 1 }, // Inestable
    { id: 9, nombre: 'Miguel', apellido: 'Sánchez', estado: 2 }, // Estable
    { id: 10, nombre: 'Isabella', apellido: 'Torres', estado: 0 }, // Grave
    { id: 11, nombre: 'Diego', apellido: 'Peralta', estado: 1 }, // Inestable
    { id: 12, nombre: 'Valentina', apellido: 'Vargas', estado: 2 }, // Estable
    { id: 13, nombre: 'Javier', apellido: 'Hernández', estado: 0 }, // Grave
    { id: 14, nombre: 'Elena', apellido: 'Rojas', estado: 1 }, // Inestable
    { id: 15, nombre: 'Andrés', apellido: 'Molina', estado: 2 }, // Estable
    { id: 16, nombre: 'Lucía', apellido: 'Paz', estado: 0 }, // Grave
    { id: 17, nombre: 'Alejandro', apellido: 'Silva', estado: 1 }, // Inestable
    { id: 18, nombre: 'Camila', apellido: 'Castro', estado: 2 }, // Estable
    { id: 19, nombre: 'Mateo', apellido: 'Gutiérrez', estado: 0 }, // Grave
    { id: 20, nombre: 'Valeria', apellido: 'Mendez', estado: 1 }, // Inestable
  ];
  pacientes.sort((a, b) => a.estado - b.estado);
  */
  return (
    <View style={styles.Container}>
      <View style={styles.TitleContainer}>
        <Text style={styles.Title}>Lista de pacientes</Text>
      </View>
      <View style={styles.ListContainer}>
        <View style={styles.titleList}>
        <Text style={styles.estadoText}>Estado</Text>
        <Text style={styles.estadoText}>Nombre</Text>
        <Text style={styles.estadoText}>Acción</Text>
        </View>
        <View style={styles.line}></View>
        <View style={styles.SafeAreaItem}>
        <FlatList
          data={List}
          keyExtractor={(item) => item.id.toString()}
          renderItem={({ item }) => <Patient_List_Item paciente={item} />}
        />
        </View>
      </View>
    </View>
  )
}

export default Patient_List
const styles = StyleSheet.create({
  chatbox:{
    width: "100%",
    marginTop: "5%",
  },
  SafeAreaItem:{
    marginTop: "5%",
    width: "90%",
    height: "87%",
    marginLeft: "5%",
  },
  estadoText: {
    marginRight: "25%",
    fontWeight: "bold",
    color: 'white',
  },
  line:{
    backgroundColor:"white",
    width:"88%",
    height: ".5%",
    marginLeft: "5%",
  },
  titleList:{
    width: "86%",
    height: "5%",
    marginTop: "3%",
    marginLeft: "6%",
    flexDirection: "row",
  },
  Title:{
    fontWeight: "bold",
    fontSize: 26,
  },
  TitleContainer: {
    alignContent: "center",
    justifyContent: 'center',
    marginTop: "10%",
  },
  ListContainer: {
    backgroundColor: "#45C3CC",
    width: "80%",
    height: "72%",
    marginTop: "10%",
    borderRadius: 25,

  },
  Container: {
    width: "100%",
    height: "100%",
    alignItems: 'center',
    flexDirection: "column",
  },
});