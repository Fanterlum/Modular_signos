import React, { useState } from 'react';
import { View, Text, StyleSheet, Button,ScrollView, TouchableOpacity } from 'react-native';
import FontAwesomeIcon from 'react-native-vector-icons/FontAwesome'


const ChatMessage = ({ messages , isVisibleProp,handleButtonClick, setCapa1, setCapa2, capa1}) => {
 
  const handleCapa1Click = () => {
    setCapa1(true);
  };

  const handleCapa2Click = () => {
    setCapa2(true);
  };    

  return (
    <ScrollView >
      {isVisibleProp && (
        <View style={styles.containerPaciente}>
          <TouchableOpacity
            style={styles.chatboxPaciente}
            onPress={()=>{handleButtonClick(); handleCapa1Click();}}
          >
            <View style={styles.buttonContent}>
              <FontAwesomeIcon
                name='user-circle-o'
                size={25}
                color={'#fff'}
              />
              <Text style={styles.textButtons}> 
                Paciente
              </Text>
            </View>
            
          </TouchableOpacity>
        </View>
        
      )}
      {isVisibleProp && (
        <View style={styles.containerPregunta}>
          <TouchableOpacity
            style={styles.chatboxPregunta}
            onPress={()=>{handleButtonClick(); handleCapa2Click();}}
            >
              <View style={styles.buttonContent}>
                <FontAwesomeIcon
                  name='question-circle'
                  size={25}
                  color={'#fff'}
                />
                <Text style={styles.textButtons}> 
                  Pregunta
                </Text>
              </View>
              
          </TouchableOpacity>
        </View>
        
      )}
      
      {messages.map((msg, index) => (
        <View
          style={[
            styles.messageItem,
            {
              alignSelf: msg.name === 'User' ? 'flex-end' : 'flex-start',
            },
          ]}
          key={index}
        >
          <Text style={styles.messageText}>{msg.message}</Text>
        </View>
      ))}
    </ScrollView>
  );
};


const styles = StyleSheet.create({
  buttonContent: {
    flexDirection: 'row', // Arrange icon and text in a row
    alignItems: 'center', // Align items vertically
  },
  textButtons:{
    color: '#fff',
    fontSize: 16, 
    paddingLeft: 10,
  },
  containerPaciente: {
    flex: 1,
    justifyContent: 'center', // Center the icon vertically
    alignItems: 'center', // Center the icon horizontally
    marginBottom: 20, 
    paddingTop: 25
  },
  containerPregunta: {
    flex: 1,
    justifyContent: 'center', // Center the icon vertically
    alignItems: 'center', // Center the icon horizontally
    marginBottom: 20, 
  },
  messageContainer: {
    flexDirection: 'column',
    padding: 10,
  },
  messageItem: {
    backgroundColor: '#e0e0e0',
    padding: 10,
    marginVertical: 4,
    marginHorizontal: 8,
    borderRadius: 20,
    maxWidth: '70%',
  },
  messageText: {
    fontSize: 16,
  },
  chatboxPaciente: {  
    backgroundColor: '#3449eb',
    padding: 10,
    borderRadius: 20,
    paddingHorizontal: 50
  },
  chatboxPregunta: {  
    backgroundColor: '#3449eb',
    padding: 10,
    borderRadius: 20,
    paddingHorizontal: 50
  },
});


export default ChatMessage;