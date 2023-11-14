import React from 'react';
import { Text, View, StyleSheet } from 'react-native';
import FontAwesomeIcon from 'react-native-vector-icons/FontAwesome';

const ChatboxHeader = () => {
  return (
    <View style={styles.containerElementsHeader}>
              <FontAwesomeIcon
          name='heartbeat'
          size={35}
          color={'#fff'}
        />
      <View style={styles.containerHeader}>
        <Text style={styles.heading}>Virtual Monitor</Text>
        <Text style={styles.description}>Chatbot médico | ¿Qué deseas hacer?</Text>
      </View>
    </View>
    
  );
};

const styles = StyleSheet.create({
  containerElementsHeader: {
    flexDirection: 'row', // Stack elements vertically
    alignItems: 'center', // Align elements horizontally
    backgroundColor: '#3449eb',
    paddingLeft: 10,
    borderRadius: 8,
    
  },
  containerHeader: {
    flexDirection: 'column', // Stack elements vertically
    alignItems: 'center', // Align elements horizontally
    paddingVertical: 10, // Add vertical padding as needed
    paddingLeft: 15,
  },
  iconHeader: {
    paddingRight: 8
  },
  containerText: {
    flexDirection: 'column', // Stack elements vertically
    alignItems: 'center', // Align elements horizontally
  },
  heading: {
    fontSize: 16, // Adjust font size as needed
    fontWeight: 'bold',
    marginBottom: 5, // Add vertical margin as needed
    color: '#fff'
  },
  description: {
    fontSize: 12, // Adjust font size as needed
    color: '#fff'
  },
});

export default ChatboxHeader;
