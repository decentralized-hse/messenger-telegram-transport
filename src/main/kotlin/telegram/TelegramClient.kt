package telegram

import io.ktor.client.*
import io.ktor.client.call.*
import io.ktor.client.engine.*
import io.ktor.client.engine.cio.*
import io.ktor.client.request.*
import io.ktor.http.*
import kotlinx.coroutines.runBlocking
import kotlinx.serialization.decodeFromString
import kotlinx.serialization.encodeToString
import kotlinx.serialization.json.Json
import java.util.*

class TelegramClient(
    private val channelName: String,
    engine: HttpClientEngine = CIO.create(),
) {
    private val httpClient = HttpClient(engine)

    fun send(botToken: String, senderId: String, text: String) = runBlocking {
        val message = Json.encodeToString(Message(senderId, text))
        val encodedMessage = Base64.getEncoder().encodeToString(message.toByteArray())
        val response = httpClient.post("https://api.telegram.org/bot$botToken/sendMessage") {
            contentType(ContentType.Application.Json)
            setBody(mapOf("chat_id" to "@$channelName", "text" to encodedMessage))
        }
        if (response.status != HttpStatusCode.OK) {
            throw RuntimeException("Telegram Bot API Error: $response")
        }
        println("Send message from $senderId: $text")
    }

    fun read(): Message = runBlocking {
        val response = httpClient.get("https://t.me/s/$channelName").body<String>()
            .substringAfterLast("""<div class="tgme_widget_message_text js-message_text" dir="auto">""")
            .substringBefore("""</div>""")
        val decodedMessage = String(Base64.getDecoder().decode(response))
        val message = Json.decodeFromString<Message>(decodedMessage)
        println("Got message from ${message.senderId}: ${message.text}")
        return@runBlocking message
    }
}