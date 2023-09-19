import React, { useState } from 'react';
import { View, Text, TouchableOpacity, StyleSheet, Image, PixelRatio} from 'react-native';
import Chatbox from './Chatbox/Chatbox';
//Foto del bot


const ButtonChatbox = () => {
  const [showChatbox, setShowChatbox] = useState(false);

  const handleButtonPress = () => {
    setShowChatbox(!showChatbox);
  };
  const botPhoto = require('../../assets/bot-icon.png');
  //Tamaño responsive para el bot
  const responsivePhoto = PixelRatio.getPixelSizeForLayoutSize(20); // 50 DP
  return (
    <View style={styles.container}>
      {showChatbox && <Chatbox />}
      <TouchableOpacity
        style={styles.chatboxButton}
        onPress={handleButtonPress}
      >
        <Image source={botPhoto} style={[{height: responsivePhoto}, {width: responsivePhoto}]}
                resizeMode="contain" // Controla cómo se ajusta la imagen
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
    marginBottom: "3%", // Adjust the margin as needed
    marginRight: "5%", // Adjust the margin as needed
  },
  chatboxButton: {
    padding: "3%",
  },
});

export default ButtonChatbox;
