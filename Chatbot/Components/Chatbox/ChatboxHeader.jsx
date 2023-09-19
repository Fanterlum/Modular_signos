import React from 'react';
import { Text, View, StyleSheet } from 'react-native';
import FontAwesomeIcon from 'react-native-vector-icons/FontAwesome';

const ChatboxHeader = () => {
  return (
    <View style={styles.containerHeader}>
      <Text style={styles.heading}>Virtual Monitor</Text>
      <Text style={styles.description}>Chatbot médico | ¿Qué deseas hacer?</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  containerHeader: {
    flexDirection: 'column', // Stack elements vertically
    alignItems: 'center', // Align elements horizontally
    paddingVertical: 8, // Add vertical padding as needed
    backgroundColor: '#CFD8DC',
  },
  iconHeader: {
    paddingRight: "5%",
  },
  containerText: {
    flexDirection: 'column', // Stack elements vertically
    alignItems: 'center', // Align elements horizontally
  },
  heading: {
    fontSize: 16, // Adjust font size as needed
    fontWeight: 'bold',
    marginBottom: "2%", // Add vertical margin as needed
  },
  description: {
    fontSize: 12, // Adjust font size as needed
  },
});

export default ChatboxHeader;
