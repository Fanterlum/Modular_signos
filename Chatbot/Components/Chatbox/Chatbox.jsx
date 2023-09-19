import React, { useState } from 'react'
import ChatboxHeader from './ChatboxHeader'
import ChatMessage from './ChatMessage'
import { StyleSheet, View } from 'react-native'
import ChatboxFooter from './ChatboxFooter'
import axios from 'axios';


const Chatbox = () => {

  const [messages, setMessages] = useState([]);
  const [showLayers, setShowLayers] = useState(false);
  const [inputText, setInputText] = useState('');

  const toggleLayers = () => {
    setShowLayers(!showLayers);
  };

  const onSendButton = async () => {
    if (!inputText) return;
  
    const userMessage = { name: 'User', message: inputText };
    setMessages([...messages, userMessage]);
  
    try {
      const response = await axios.post('http://localhost:5000/status', { message: inputText });
      const samMessage = { name: 'Sam', message: response.data.answer };
      setMessages(prevMessages => [...prevMessages, samMessage]); // Update messages array
      setInputText(''); // Clear the input text after sending
    } catch (error) {
      console.error('Error:', error.message);
    }
  };

  return (
    <View style={styles.container}>
        <ChatboxHeader></ChatboxHeader>
        <ChatMessage messages={messages}></ChatMessage>
        <ChatboxFooter
          onSendButton={onSendButton}
          toggleLayers={toggleLayers}
          showLayers={showLayers}
          inputText={inputText} 
          setInputText={setInputText}>
        </ChatboxFooter>
    </View>

  )
}

const styles = StyleSheet.create({
    container: {
        borderWidth: 1,
        borderColor: '#fff',
        borderRadius: 25,
        marginBottom: "3%",
    },
});

export default Chatbox