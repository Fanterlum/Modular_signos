import React, { useState } from 'react'
import ChatboxHeader from './ChatboxHeader'
import ChatMessage from './ChatMessage'
import { StyleSheet, View } from 'react-native'
import ChatboxFooter from './ChatboxFooter'
import axios from 'axios';
import { Constants } from 'expo-constants'
const Chatbox = () => {
  const Url = Constants?.expoConfig?.extra?.chatbotUrl;
  const defaultMessage = { name: 'Info', message: 'Disculpa, en este momento tengo problemas para conectarme a internet. Inténtalo después.' };
  const [messages, setMessages] = useState([]);
  const [showLayers, setShowLayers] = useState(false);
  const [inputText, setInputText] = useState('');
  const [isChatMessageVisible, setIsChatMessageVisible] = useState(true);
  const [isTextboxVisible, setIsTextboxVisible] = useState(false);
  const [capa1, setCapa1] = useState(false);
  const [capa2, setCapa2] = useState(false);

  const showDefaultMessage = () => {
    setMessages([defaultMessage]);
  };
  //const [Return, setCapa2] = useState(false);

  const toggleLayers = () => {
    setShowLayers(!showLayers);
  };
  

  const toggleChatMessageVisibility = () => {
    setIsChatMessageVisible(!isChatMessageVisible);
  };

  const toggleTextboxVisibility = () => {
    setIsTextboxVisible(!isTextboxVisible);
  };

  const handleButtonClick = () => {
    showDefaultMessage();
    toggleChatMessageVisibility();
    toggleTextboxVisibility(); 
  };
  

  const onSendButton = async () => {
    if (!inputText) return;
  
    const userMessage = { name: 'User', message: inputText };
    setMessages([...messages, userMessage]);
    /*
    try {
      // const response = await globalThis.fetch('http://localhost:5000/status', {
      const response = await globalThis.fetch(`${Url}/status`, {
        method: 'POST',
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json'  
        },
        body: JSON.stringify({ message: inputText }),
      });
  
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
  
      const responseData = await response.json();
      const samMessage = { name: 'Sam', message: responseData.answer };
      setMessages(prevMessages => [...prevMessages, samMessage]);
      setInputText('');
    } catch (error) {
      console.error('Error:', error.message);
    }
    */

  };
  const onSendButton2 = async () => {
    if (!inputText) return;
  
    const userMessage = { name: 'User', message: inputText };
    setMessages([...messages, userMessage]);
  /*
    try {
      // const response = await globalThis.fetch('http://localhost:5000/status', {
      const response = await globalThis.fetch('http://10.0.2.2:5000/predict', {
        method: 'POST',
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json'  
        },
        body: JSON.stringify({ message: inputText }),
      });
  
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
  
      const responseData = await response.json();
      const samMessage = { name: 'Sam', message: responseData.answer };
      setMessages(prevMessages => [...prevMessages, samMessage]);
      setInputText('');
    } catch (error) {
      console.error('Error:', error.message);
    }
    */
  };


  return (
    <View style={styles.container}>
        <ChatboxHeader></ChatboxHeader>
        <ChatMessage 
          messages={messages} 
          isVisibleProp={isChatMessageVisible}
          handleButtonClick={handleButtonClick}
          setCapa1={setCapa1}
          setCapa2={setCapa2}
          capa1={capa1}>
        </ChatMessage>
        <ChatboxFooter
          setCapa1={setCapa1}
          setCapa2={setCapa2}
          handleButtonClick={handleButtonClick}
          isTextboxVisible={isTextboxVisible}
          toggleChatMessageVisibility={toggleChatMessageVisibility}
          onSendButton={() => { showDefaultMessage(); onSendButton(); }}
          onSendButton2={() => { showDefaultMessage(); onSendButton2(); }}
          toggleLayers={toggleLayers}
          showLayers={showLayers}
          inputText={inputText} 
          setInputText={setInputText}
          setMessages={setMessages}
          capa1={capa1}>
        </ChatboxFooter>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
      borderWidth: 1,
      borderColor: 'white',
      borderRadius: 9,
      marginBottom: 8,
      minHeight: '60%',
      maxWidth: '80%',
      minWidth: '70%',
      maxHeight: '80%'
  },
});

export default Chatbox