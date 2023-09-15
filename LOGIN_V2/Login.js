import React, { useState } from "react";
import {
  Text,
  View,
  Image,
  StyleSheet,
  TextInput,
  Button,
  Alert,
  TouchableOpacity,
} from 'react-native'
import logo from './assets/LOGO.png'
import { useNavigation } from "@react-navigation/native";

const Login = () => {
  const navigation = useNavigation();

  const [Correo, setCorreo] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = () => {
    if (Correo === 'Admin' && password === '12345') {
      console.log('Credenciales correctas');
      navigation.push('Home'); // Navegar a la pantalla HomeScreen
    } else {
      Alert.alert('Correo y/o contraseña incorrecta!!');
    }
  };

  const handleRegistro = () => {
    navigation.push('Registro');
  };

  return (
    <View style={styles.container}>
      <Image
        source={logo}
        style={styles.image}
      />
      <Text style={styles.title}>Login</Text>
      <TextInput
        style={styles.formulario}
        placeholder="tuCorreo@ejemplo.com"
        value={Correo}
        onChangeText={setCorreo}
      />
      <TextInput
        style={styles.formulario}
        placeholder="Contraseña"
        secureTextEntry
        value={password}
        onChangeText={setPassword}
      />
      <Button title="Iniciar Sesión" onPress={handleLogin} color='#1C2B2E' />
      <TouchableOpacity style={styles.button} onPress={handleRegistro}>
      <Text>{'\n'}</Text>
        <Text style={styles.boton_registro}>¿No tienes cuenta? Regístrate aquí.</Text>
      </TouchableOpacity>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#B4E2E5',
    padding: 20,
  },
  title: {
    fontSize: 30,
    color: 'black',
    marginBottom: 20,
    fontWeight: 'bold',
  },
  image: {
    height: '25%', // Utiliza un porcentaje del alto de la pantalla
    aspectRatio: 1, // Mantiene la proporción original
    //marginBottom: 20,
    borderRadius: 30,
  },
  formulario: {
    width: '80%',
    height: 40,
    borderColor: 'gray',
    borderWidth: 1,
    marginBottom: 20,
    paddingLeft: 10,
    borderRadius: 70,
    backgroundColor: 'white',
  },
  boton_registro: {
    fontSize: 17,
    color: '#1C2B2E', // Cambia el color del texto del botón de registro
    fontWeight: 'bold',
  },
});

export default Login;
