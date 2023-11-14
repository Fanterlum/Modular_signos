import React, { useState } from 'react';
import { View, Text, TouchableOpacity, StyleSheet } from 'react-native';
import Chatbox from './Chatbox/Chatbox';
import FontAwesomeIcon from 'react-native-vector-icons/FontAwesome'

const ButtonChatbox = () => {
  const [showChatbox, setShowChatbox] = useState(false);

  const handleButtonPress = () => {
    setShowChatbox(!showChatbox);
  };

  return (
    <View style={styles.container}>
      {showChatbox && <Chatbox />}
      <TouchableOpacity
        style={styles.chatboxButton}
        onPress={handleButtonPress}
      >
        <FontAwesomeIcon
          name='comments-o'
          size={25}
          color={'#fff'}
        />
        
      </TouchableOpacity>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'flex-end', // Align the button and chatbox to the bottom
    alignItems: 'flex-end', // Align the button and chatbox to the right
    marginBottom: 20, // Adjust the margin as needed
    marginRight: 20, // Adjust the margin as needed
  },
  chatboxButton: {  
    backgroundColor: '#3449eb',
    padding: 10,
    borderRadius: 20,
  },
});

export default ButtonChatbox;
