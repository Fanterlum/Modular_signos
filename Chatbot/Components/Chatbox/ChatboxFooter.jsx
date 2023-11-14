import React, { useState } from 'react';
import { Text, View, TextInput, TouchableOpacity, StyleSheet } from 'react-native';

const ChatboxFooter = ({ inputText, 
                        setInputText, 
                        onSendButton,
                        onSendButton2,
                        isTextboxVisible,
                        handleButtonClick,
                        setCapa1,
                        setCapa2, 
                        capa1,
                        setMessages}) => 
  {
  const handleCapasClick = () => {
    // Use setCapa1 function here
    setCapa1(false);
    setCapa2(false);
  };

  const resetMessages = () => {
    setMessages([]);
  }

  return (
    <View style={styles.container}>
      {isTextboxVisible &&
      <>
        <TextInput
          placeholder="Escribe un mensaje"
          placeholderTextColor="#fff" 
          style={styles.input}
          value={inputText}
          onChangeText={(e) => setInputText(e)}
        />
        
        <TouchableOpacity
          style={styles.buttonSend}
          onPress={capa1 ? onSendButton : onSendButton2}
        >
          <Text style={styles.buttonText}>Send</Text>
        </TouchableOpacity>
        <TouchableOpacity
          onPress={()=> {handleButtonClick(); handleCapasClick(); resetMessages();}}
          style={styles.buttonSend}
        >
          <Text style={styles.buttonText}>Return</Text>
        </TouchableOpacity>
      </> 
      }
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flexDirection: 'row', 
    alignItems: 'center', 
    padding: 8, 
    backgroundColor: '#3449eb',
    borderRadius: 8,
  },
  input: {
    marginRight: 8, 
    borderWidth: 1,
    borderColor: '#fff',
    color: '#fff',
    borderRadius: 5,
    padding: 7,
    maxWidth: '54%'
  },
  buttonSend: {
    backgroundColor: 'cornflowerblue',
    padding: 8,
    borderRadius: 20,
    marginRight: 5
  },
  buttonText: {
    color: 'white',
    fontWeight: 'bold',
  },
});

export default ChatboxFooter;
