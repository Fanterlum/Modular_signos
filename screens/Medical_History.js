import React, { useState, useEffect } from 'react';
import { View, StyleSheet, ActivityIndicator, ScrollView } from 'react-native';
import Svg, { Line, Circle, Rect, Text } from 'react-native-svg';
import { Text as RNText } from 'react-native';
import GetGraph from '../backend/GetGraph';

const MedicalHistoryGraph = ({ SignalData }) => {
  const graphWidth = SignalData.PUNTO_FINAL_X + 10;
  const graphHeight = 300;
  const backgroundColor = 'white';
  const gridLineColor = 'red';
  const gridSize = 20;

  const generateGridLines = () => {
    const lines = [];

    for (let y = gridSize; y < graphHeight; y += gridSize) {
      lines.push(
        <Line key={`h${y}`} x1="0" y1={y} x2={graphWidth} y2={y} stroke={gridLineColor} strokeWidth="1" strokeOpacity="0.5" />
      );
    }

    for (let x = gridSize; x < graphWidth; x += gridSize) {
      lines.push(
        <Line key={`v${x}`} x1={x} y1="0" x2={x} y2={graphHeight} stroke={gridLineColor} strokeWidth="1" strokeOpacity="0.5" />
      );
    }

    return lines;
  };

  return (
    <View>
      <Svg width={graphWidth} height={graphHeight}>
        <Rect x="0" y="0" width={graphWidth} height={graphHeight} fill={backgroundColor} />
        {generateGridLines()}
        <Line x1={SignalData.PRIMER_PUNTO_X} y1={SignalData.PRIMER_PUNTO_Y} x2={SignalData.P_SIGNAL_X} y2={SignalData.P_SIGNAL_Y} stroke="black" strokeWidth="2" />
        <Line x1={SignalData.P_SIGNAL_X} y1={SignalData.P_SIGNAL_Y} x2={SignalData.Q_SIGNAL_X} y2={SignalData.Q_SIGNAL_Y} stroke="black" strokeWidth="2" />
        <Line x1={SignalData.Q_SIGNAL_X} y1={SignalData.Q_SIGNAL_Y} x2={SignalData.PUNTO_MAS_ALTO_X} y2={SignalData.PUNTO_MAS_ALTO_Y} stroke="black" strokeWidth="2" />
        <Line x1={SignalData.PUNTO_MAS_ALTO_X} y1={SignalData.PUNTO_MAS_ALTO_Y} x2={SignalData.S_SIGNAL_X} y2={SignalData.S_SIGNAL_Y} stroke="black" strokeWidth="2" />
        <Line x1={SignalData.S_SIGNAL_X} y1={SignalData.S_SIGNAL_Y} x2={SignalData.T_SIGNAL_X} y2={SignalData.T_SIGNAL_Y} stroke="black" strokeWidth="2" />
        <Line x1={SignalData.T_SIGNAL_X} y1={SignalData.T_SIGNAL_Y} x2={SignalData.PUNTO_FINAL_X} y2={SignalData.PUNTO_FINAL_Y} stroke="black" strokeWidth="2" />

        <Circle cx={SignalData.PRIMER_PUNTO_X} cy={SignalData.PRIMER_PUNTO_Y} r="4" fill="red" />
        <Circle cx={SignalData.PUNTO_MAS_ALTO_X} cy={SignalData.PUNTO_MAS_ALTO_Y} r="4" fill="red" />
        <Circle cx={SignalData.PUNTO_FINAL_X} cy={SignalData.PUNTO_FINAL_Y} r="4" fill="red" />
        <Circle cx={SignalData.Q_SIGNAL_X} cy={SignalData.Q_SIGNAL_Y} r="4" fill="red" />
        <Circle cx={SignalData.S_SIGNAL_X} cy={SignalData.S_SIGNAL_Y} r="4" fill="red" />
        <Circle cx={SignalData.T_SIGNAL_X} cy={SignalData.T_SIGNAL_Y} r="4" fill="red" />
        <Circle cx={SignalData.P_SIGNAL_X} cy={SignalData.P_SIGNAL_Y} r="4" fill="red" />
        <Text x={SignalData.PUNTO_MAS_ALTO_X + 1} y={SignalData.PUNTO_MAS_ALTO_Y - 5} fontSize="12" fontWeight="bold" fill="black">
          R
        </Text>
        <Text x={SignalData.Q_SIGNAL_X + 1} y={SignalData.Q_SIGNAL_Y + 13} fontSize="12" fontWeight="bold" fill="black">
          Q
        </Text>
        <Text x={SignalData.S_SIGNAL_X + 1} y={SignalData.S_SIGNAL_Y + 13} fontSize="12" fontWeight="bold" fill="black">
          S
        </Text>
        <Text x={SignalData.T_SIGNAL_X + 1} y={SignalData.T_SIGNAL_Y - 5} fontSize="12" fontWeight="bold" fill="black">
          T
        </Text>
        <Text x={SignalData.P_SIGNAL_X + 1} y={SignalData.P_SIGNAL_Y - 5} fontSize="12" fontWeight="bold" fill="black">
          P
        </Text>
      </Svg>
    </View>
  );
};

const Statistics = ({ route }) => {
  const userId = route.params?.userId;
  const [lastRecord, setLastRecord] = useState();
  const [weeklyAverage, setWeeklyAverage] = useState();

  useEffect(() => {
    const fetchDataWithId = async (id) => {
      try {
        // Simulación de datos de electrocardiograma para el último registro
        const lastRecordData = {
          PRIMER_PUNTO_X: 30,
          PRIMER_PUNTO_Y: 150,
          P_SIGNAL_X: 70,
          P_SIGNAL_Y: 120,
          Q_SIGNAL_X: 110,
          Q_SIGNAL_Y: 180,
          PUNTO_MAS_ALTO_X: 150,
          PUNTO_MAS_ALTO_Y: 90,
          S_SIGNAL_X: 190,
          S_SIGNAL_Y: 170,
          T_SIGNAL_X: 230,
          T_SIGNAL_Y: 130,
          PUNTO_FINAL_X: 270,
          PUNTO_FINAL_Y: 150,
           // Llama a la función GetInfo para obtener datos basados en el ID
          //const jsonData = await GetGraph(id);
          //setSignalData(jsonData);
          // Puedes actualizar otras variables de estado según sea necesario
        };
        setLastRecord(lastRecordData);

        // Simulación de datos de electrocardiograma para el promedio semanal
        const weeklyAverageData = {
          PRIMER_PUNTO_X: 45,
          PRIMER_PUNTO_Y: 170,
          P_SIGNAL_X: 90,
          P_SIGNAL_Y: 130,
          Q_SIGNAL_X: 100,
          Q_SIGNAL_Y: 190,
          PUNTO_MAS_ALTO_X: 160,
          PUNTO_MAS_ALTO_Y: 100,
          S_SIGNAL_X: 200,
          S_SIGNAL_Y: 180,
          T_SIGNAL_X: 240,
          T_SIGNAL_Y: 140,
          PUNTO_FINAL_X: 290,
          PUNTO_FINAL_Y: 170,
          // Llama a la función GetInfo para obtener datos basados en el ID
          //const jsonData = await GetGraph(id);
          //setSignalData(jsonData);
          // Puedes actualizar otras variables de estado según sea necesario
        };
        setWeeklyAverage(weeklyAverageData);
      } catch (error) {
        console.error('Error al obtener el JSON:', error);
      }
    };
    fetchDataWithId(userId);
  }, [userId]);

  console.log(lastRecord);
  console.log(weeklyAverage);

  return (
    <ScrollView style={styles.scrollView}>
      {/* Último registro */}
      <View style={styles.titlecontainer}>
        <RNText style={styles.title}>Historial semanal</RNText>
      </View>
      <View style={styles.container}>
        {lastRecord ? (
          <>
            <RNText style={styles.Textonormal}>Señal Actual</RNText>
            <MedicalHistoryGraph SignalData={lastRecord} />
            <RNText style={styles.Textonormal}>Oxigenacion: {'90'}</RNText>
            <RNText style={styles.Textonormal}>Ritmo cardiaco: {'85'}</RNText>
            <RNText style={styles.Textonormal}>Frecuencia respiratoria: {'95'}</RNText>
            {/* Agrega aquí el código para mostrar el promedio semanal 
            <RNText style={styles.Textonormal}>Oxigenacion: {SignalData.OXIGENACION}</RNText>
            <RNText style={styles.Textonormal}>Ritmo cardiaco: {SignalData.RITMOCARDIACO}</RNText>
            <RNText style={styles.Textonormal}>Frecuencia respiratoria: {SignalData.RESP}</RNText>
            */}
          </>
        ) : (
          <ActivityIndicator />
        )}
      </View>

      {/* Promedio semanal */}
      <View style={styles.titlecontainer}>
        <RNText style={styles.title}>Promedio semanal</RNText>
      </View>
      <View style={styles.container}>
        {weeklyAverage ? (
          <>
            <MedicalHistoryGraph SignalData={weeklyAverage} />
            <RNText style={styles.Textonormal}>Oxigenacion: {'95'}</RNText>
            <RNText style={styles.Textonormal}>Ritmo cardiaco: {'70'}</RNText>
            <RNText style={styles.Textonormal}>Frecuencia respiratoria: {'80'}</RNText>
            {/* Agrega aquí el código para mostrar el promedio semanal 
            <RNText style={styles.Textonormal}>Oxigenacion: {SignalData.OXIGENACION}</RNText>
            <RNText style={styles.Textonormal}>Ritmo cardiaco: {SignalData.RITMOCARDIACO}</RNText>
            <RNText style={styles.Textonormal}>Frecuencia respiratoria: {SignalData.RESP}</RNText>
            */}
          </>
        ) : (
          <ActivityIndicator />
        )}
      </View>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  scrollView: {
    flex: 1,
    backgroundColor: 'white',
  },
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    height: '75%',
    backgroundColor: 'white',
  },
  titlecontainer: {
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: 'white',
  },
  title: {
    fontSize: 28,
    fontWeight: 'bold',
    marginTop: '5%',
  },
  Textonormal: {
    fontSize: 18,
    fontWeight: 'bold',
    marginTop: '2%',
  },
});

export default Statistics;
