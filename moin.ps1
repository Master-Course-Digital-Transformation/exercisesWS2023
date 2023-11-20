# Funktion, um die aktuelle Uhrzeit abzurufen
function Get-TimeOfDay {
    $currentTime = Get-Date
    $hour = $currentTime.Hour

    if ($hour -ge 5 -and $hour -lt 10) {
        return "Morgen"
    }
    elseif ($hour -ge 10 -and $hour -lt 17) {
        return "Tag"
    }
    elseif ($hour -ge 17 -and $hour -lt 22) {
        return "Abend"
    }
    else {
        return "Nacht"
    }
}

# Begrüßungsnachricht erstellen
function Get-GreetingMessage {
    $timeOfDay = Get-TimeOfDay
    $additionalMessage = "DT-M02-F01-WiSe-2023"
    return "Guten $timeOfDay! $additionalMessage"
}

# Begrüßung ausgeben
Get-GreetingMessage