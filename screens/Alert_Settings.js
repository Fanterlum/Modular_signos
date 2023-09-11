import { View, Text, Button } from 'react-native';
import React from 'react'
import { DrawerActions } from '@react-navigation/routers';



const Alert_Settings = ({ navigation }) => {
  const openDrawer = () => {
    navigation.openDrawer();
  };
  return (
    <View>
      <Text>Pantalla personalizada</Text>
      {/* Agrega el contenido de tu pantalla */}
    </View>
  );
};

export default Alert_Settings