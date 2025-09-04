def konversi_suhu (nilai, dari, ke):
    if (dari != "C" and dari != "F" and dari != "K"):
      return "Masukkan satuan suhu yang benar"
    elif (ke != "C" and ke != "F" and ke != "K"):
      return "Masukkan satuan suhu yang benar"
    elif (nilai < 0 and dari == "k"):
      return "satuan Kelvin tidak boleh bersifat negatif"

    if (dari == "C"):
      if (ke == "F"):
        return (nilai * 9/5) + 32
      elif (ke == "K"):
        return nilai + 273.15
    elif (dari == "F"):
      if (ke == "C"):
        return (nilai - 32) * 5/9
      elif (ke == "K"):
        return (nilai - 32) * 5/9 + 273.15
    elif (dari == "K"):
      if (ke == "C"):
        return nilai - 273.15
      elif (ke == "F"):
        return (nilai - 273.15) * 9/5 + 32