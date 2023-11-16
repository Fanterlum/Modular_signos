import {ExpoConfig, ConfigContext } from 'expo/config'
import * as dotenv from 'dotenv'

dotenv.config()

export default ({ config }: ConfigContext): ExpoConfig => {
    return {
        ...config,
        slug: 'VitalSignVision',
        name: 'VitalSignVision',
        extra: {
            ...config.extra,
            backendUrl: process.env.BACKEND_URL,
            chatbotUrl: process.env.CHATBOT_URL
        }
    }
}