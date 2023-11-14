import { StyleSheet } from 'react-native';

export const styles = StyleSheet.create({
  historial:{
    position: "absolute",
    top: "-35%",
    left: "30%",
    backgroundColor: "#45C3CC",
    width: "40%",
    borderRadius: 5,
  },
  estadistica: {
    position: "absolute",
    top: "30%",
    left: "33%",
    backgroundColor: "#45C3CC",
    width: "35%",
    borderRadius: 5,
  },
  StatusText: {
      fontWeight: "bold",
      fontSize: 18,
    },
    buttonText: {
      color: "white",
      fontWeight: "bold",
      fontSize: 20,
    },
    button: {
      backgroundColor: "#45C3CC",
      justifyContent: 'center',
      alignItems: 'center',
      marginLeft: "35%",
      marginBottom: "10%",
      width: "35%",
      height: "45%",
      borderRadius: 5,
    },
    buttonChat: {
      justifyContent: 'center',
      alignItems: 'center',
      marginLeft: "2%",
      marginRight: "5%",
      width: "25%"
    },
    buttonChat2: {
        justifyContent: 'center',
        alignItems: 'center',
        marginLeft: "72%",
        marginRight: "5%",
        width: "25%"
      },
    estados: {
      width: "60%",
      height: "30%",
      marginLeft: "20%",
      borderRadius: 15,
      marginTop: "3%",
      alignItems: 'center',
      justifyContent: 'center',
    },
    titleText: {
      fontSize: 24,
      marginBottom: "3%",
      marginTop: "2%",
      fontWeight: "bold",
    },
    PatientPhoto: {
      width: "50%",
      height: "85%",
      borderRadius: 100,
    },
    botContainer: {
      position: 'absolute',
      bottom: 0,
      left: 0,
      right: 0,
      // Otros estilos para botContainer
    },
    buttonChatboxContainer: {
      position: 'absolute',
      bottom: '50%', // Coloca ButtonChatbox en la mitad de la pantalla
      left: 0,
      right: 0,
      // Otros estilos para el contenedor de ButtonChatbox si es necesario
    },
    DataText: {
      marginTop: "2%",
      fontSize: 24,
    },
    DataText2: {
      marginTop: "8%",
      fontSize: 24,
    },
    MainContainer: {
      width: "100%",
      height: "100%",
      backgroundColor: "white",
    },
    photoContainer: {
      alignItems: 'center',
      justifyContent: 'top',
      width: "100%",
      height: "35%",
      flexDirection: "column",
    },
    infoContainer: {
      width: "100%",
      height: "30%",
      alignItems: 'center',
      justifyContent: 'top',
      flexDirection: "column",
    },
    Patient_StatusContainer: {
      width: "100%",
      height: "25%",
    },
    chatbotContainer: {
      width: "100%",
      height: "10%",
      flexDirection: "row",
      alignItems: 'center',
      justifyContent: 'center',
    },
  });