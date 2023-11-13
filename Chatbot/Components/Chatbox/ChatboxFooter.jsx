import React, { useState } from 'react';
import { Text, View, TextInput, TouchableOpacity, StyleSheet } from 'react-native';

const ChatboxFooter = ({ inputText, setInputText, onSendButton }) => {

  return (
    <View style={styles.container}>
      <TextInput
        placeholder="Escribe un mensaje"
        style={styles.input}
        value={inputText}
        onChangeText={(e) => setInputText(e)}
      />
      <TouchableOpacity
        style={styles.buttonSend}
        onPress={onSendButton}
      >
        <Text style={styles.buttonText}>Send</Text>
      </TouchableOpacity>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flexDirection: 'row', // Arrange elements horizontally
    alignItems: 'center', // Align elements vertically
    padding: "5%", // Add horizontal padding as needed
    backgroundColor: '#CFD8DC',
  },
  input: {
    // flex: 1, // Take up the remaining space
    marginRight: "3%", // Add right margin for spacing between input and buttons
    borderWidth: 1,
    borderColor: 'black',
    backgroundColor: "white",
    borderRadius: 20,
    padding: "2%",
  },
  buttonSend: {
    backgroundColor: '#03A9F4',
    padding: "5%",
    borderRadius: 15,
    marginRight: "0.5%",
  },
  buttonText: {
    color: 'white',
    fontWeight: 'bold',
  },
});

export default ChatboxFooter;
