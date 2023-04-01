package telegram

import kotlinx.serialization.Serializable

@Serializable
data class Message(
    val senderId: String,
    val text: String
)
