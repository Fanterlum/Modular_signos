import { View, Text, Button, TouchableOpacity, PixelRatio} from 'react-native';
import React from 'react'
import { DrawerActions } from '@react-navigation/routers';
import Bot_Photo from '../components/items/Bot_Photo';
import { StyleSheet } from 'react-native';

//se importa el chatbot
import ButtonChatbox from '../Chatbot/Components/ButtonChatbox';

const Dashboard = ({ navigation }) => {
  const responsiveSize = PixelRatio.getPixelSizeForLayoutSize(10); // 50 DP
  const openDrawer = () => {
    navigation.openDrawer();
  };
  return (
    <View style={styles.mainContainer}>
      <View style={styles.topContainer}>
        <Text style={[styles.title,{fontSize:responsiveSize}]}>Bienvenido Iván Gonzalez</Text>
      </View>
      <View style={styles.midContainer}>
      <TouchableOpacity style={styles.boton}>
        <Text>Boton 1</Text>
      </TouchableOpacity>
      <TouchableOpacity style={styles.boton}>
        <Text>Boton 2</Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.boton}>
          <Text>Boton 3</Text>
        </TouchableOpacity>
      </View>
      <View style={styles.botContainer}>
        <ButtonChatbox></ButtonChatbox>
      </View>
    </View>
  );
};

export default Dashboard

const styles = StyleSheet.create({
  boton:{
    backgroundColor: "black",
    width: "90%",
    height: "30%",
    margin: "2%",
  },
  mainContainer:{
    width:"100%",
    height: "100%",
  },
  topContainer:{
    width:"100%",
    height: "15%",
    backgroundColor: "red",
    justifyContent: 'center',
    alignItems: 'center',
  },
  midContainer:{
    width:"100%",
    height: "70%",
    backgroundColor: "blue",
    justifyContent: 'center',
    alignItems: 'center',
  },
  botContainer:{
    width:"100%",
    height: "15%",
    backgroundColor: "red",
    justifyContent: 'flex-end', // Align the button and chatbox to the bottom
    alignItems: 'flex-end', // Align the button and chatbox to the right
  },
  title:{
    fontWeight: "bold",
  },
})