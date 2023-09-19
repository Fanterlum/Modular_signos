import { View, Text, Image, TouchableOpacity } from 'react-native'
import React from 'react'
import { StyleSheet } from 'react-native';

const Bot_Photo = () => {
  const botPhoto = require('../../assets/bot-icon.png');
  return (
    <Image source={botPhoto} style={styles.chatbot}
              resizeMode="contain" // Controla cómo se ajusta la imagen
    />
  )
}

export default Bot_Photo


export const styles = StyleSheet.create({
    chatbot: {
        width: "60%",
        height: "90%",
      },
})