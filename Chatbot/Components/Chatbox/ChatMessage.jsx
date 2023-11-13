import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

const ChatMessage = ({ messages }) => {
  return (
    <View style={styles.container}>
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
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    //flex: 1,
    flexDirection: 'column',
    paddingHorizontal: 16,
    backgroundColor: "#CFD8DC",
  },
  messageItem: {
    backgroundColor: '#03A9F4',
    padding: "3%",
    marginVertical: "2%",
    borderRadius: 8,
    maxWidth: '70%', // Adjust the maximum width as needed
  },
  messageText: {
    fontSize: 16,
  },
});

export default ChatMessage;
