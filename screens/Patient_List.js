import { FlatList, View, Text, Button, TouchableOpacity, Image} from 'react-native';
import React from 'react';
import { StyleSheet } from 'react-native';
import Bot_Photo from '../components/items/Bot_Photo';

//Componente de cada paciente mostrado
import Patient_List_Item from '../components/items/Patient_List_Item';

//Importamos el chatbot
import ButtonChatbox from '../Chatbot/Components/ButtonChatbox';
const Patient_List = () => {
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
  const botPhoto = require('../assets/bot-icon.png');
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
          data={pacientes}
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