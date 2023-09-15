import React from "react";
import {View, Text, StyleSheet} from 'react-native'

const Home = ()=> {
  return(
    <View style={styles.container}>
      <Text style={styles.container}>HOLA PERROS</Text>
    </View>
  )
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#D4BDFA',
    fontSize: 25,
    color: 'black',
    textAlign: 'justify',
  },
});

export default Home;