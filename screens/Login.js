import React, { useState, useEffect } from "react";
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
import logo from '../assets/LOGO.png'
import { useNavigation } from "@react-navigation/native";
import Logged2 from "../backend/Logged2";
import GetInfo from "../backend/GetInfo";
/*
  Requerimientos al backend
  Es necesaria hacer la comprobacion con los datos ingresados
  sea una consulta con la base de datos o el metodo seguro a utilizar
*/
//Log del usuario y Email
import {useUser} from '../components/Context/UserProvider';
import { useEmail } from "../components/Context/EmailProvider";
import { useJson } from "../components/Context/JsonProvider";
const Login = () => {
  const { setUserID } = useUser();
  const { setEmail } = useEmail();
  const { setJson } = useJson();
  const navigation = useNavigation();

  const [Correo, setCorreo] = useState('');
  const [password, setPassword] = useState('');

  const getUserInfo = async (userID) => {
    try {
      const UserJson = await GetInfo(userID);
      setJson(UserJson);
    } catch (error) {
      console.error("Error al obtener la información del usuario:", error);
    }
  };

  const handleLogin = async () => {
    const JsonLogin = await Logged2(Correo, password);
    console.log("Esto es el completo:");
    console.log(JsonLogin);

    if (JsonLogin.logged || Correo === "admin") {
      console.log('Credenciales correctas');
      const userID = JsonLogin.id;
      setUserID(userID);
      setEmail(Correo);
      getUserInfo(userID);
      navigation.navigate('Home');
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
        keyboardType="email-address"
      />
      <TextInput
        style={styles.formulario}
        placeholder="Contraseña"
        secureTextEntry
        value={password}
        onChangeText={setPassword}
      />
      <Button title="Iniciar Sesión" onPress={handleLogin} color='#1C2B2E'/>
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
