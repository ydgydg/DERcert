using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.IO;
namespace cunchu
{
    public class Asn1Utilprocesser
    {
        private const string PemStartStr = "-----BEGIN";
        private const string PemEndStr = "-----END";
        static char[] hexDigits = { '0', '1', '2', '3', '4', '5', '6', '7',
                                    '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'};

        public static bool IsValidHexDigits(char ch)
        {
            bool retval = false;
            for (int i = 0; i < hexDigits.Length; i++)
            {
                if (hexDigits[i] == ch)
                {
                    retval = true;
                    break;
                }
            }
            return retval;
        }

        public static byte GetHexDigitsVal(char ch)
        {
            byte retval = 0;
            for (int i = 0; i < hexDigits.Length; i++)
            {
                if (hexDigits[i] == ch)
                {
                    retval = (byte)i;
                    break;
                }
            }
            return retval;
        }

        public static byte[] HexStrToBytes(string hexStr)
        {
            hexStr = hexStr.Replace(" ", "");
            hexStr = hexStr.Replace("\r", "");
            hexStr = hexStr.Replace("\n", "");
            hexStr = hexStr.ToUpper();
            if ((hexStr.Length % 2) != 0) throw new Exception("Invalid Hex string: odd length.");
            int i;
            for (i = 0; i < hexStr.Length; i++)
            {
                if (!IsValidHexDigits(hexStr[i]))
                {
                    throw new Exception("Invalid Hex string: included invalid character [" +
                        hexStr[i] + "]");
                }
            }
            int bc = hexStr.Length / 2;
            byte[] retval = new byte[bc];
            int b1, b2, b;
            for (i = 0; i < bc; i++)
            {
                b1 = GetHexDigitsVal(hexStr[i * 2]);
                b2 = GetHexDigitsVal(hexStr[i * 2 + 1]);
                b = ((b1 << 4) | b2);
                retval[i] = (byte)b;

            }
            return retval;
        }

        public static string FormatString(string inStr, int lineLen, int groupLen)
        {
            char[] tmpCh = new char[inStr.Length * 2];
            int i, c = 0, linec = 0;
            int gc = 0;
            for (i = 0; i < inStr.Length; i++)
            {
                tmpCh[c++] = inStr[i];
                gc++;
                linec++;
                if (gc >= groupLen && groupLen > 0)
                {
                    tmpCh[c++] = ' ';
                    gc = 0;
                }
                if (linec >= lineLen)
                {
                    tmpCh[c++] = '\r';
                    tmpCh[c++] = '\n';
                    linec = 0;
                }
            }
            string retval = new string(tmpCh);
            retval = retval.TrimEnd('\0');
            retval = retval.TrimEnd('\n');
            retval = retval.TrimEnd('\r');
            return retval;
        }

        public static string BytesToString(byte[] bytes)
        {
            string retval = "";
            if (bytes == null || bytes.Length < 1) return retval;
            char[] cretval = new char[bytes.Length];
            for (int i = 0, j = 0; i < bytes.Length; i++)
            {
                if (bytes[i] != '\0')
                {
                    cretval[j++] = (char)bytes[i];
                }
            }
            retval = new string(cretval);
            retval = retval.TrimEnd('\0');
            return retval;
        }
        public static byte[] StringToBytes(string msg)
        {
            byte[] retval = new byte[msg.Length];
            for (int i = 0; i < msg.Length; i++)
            {
                retval[i] = (byte)msg[i];
            }
            return retval;
        }

        public static bool IsPemFormated(string pemStr)
        {
            byte[] data = null;
            try
            {
                data = PemToBytes(pemStr);
            }
            catch
            {
                return false;
            }
            return (data.Length > 0);
        }

        /// <summary>
        /// Check if a file is PEM formated.
        /// </summary>
        /// <param name="fileName">source file name.</param>
        /// <returns>true:Yes, false:No.</returns>
        public static bool IsPemFormatedFile(string fileName)
        {
            bool retval = false;
            try
            {
                FileStream fs = new FileStream(fileName, System.IO.FileMode.Open);
                byte[] data = new byte[fs.Length];
                fs.Read(data, 0, data.Length);
                fs.Close();
                string dataStr = Asn1Utilprocesser.BytesToString(data);
                retval = IsPemFormated(dataStr);
            }
            catch
            {
                retval = false;
            }
            return retval;
        }

        /// <summary>
        /// Convert PEM formated string into <see cref="Stream"/> and set the Stream position to 0.
        /// </summary>
        /// <param name="pemStr">source string.</param>
        /// <returns>output stream.</returns>
        public static Stream PemToStream(string pemStr)
        {
            byte[] bytes = PemToBytes(pemStr);
            MemoryStream retval = new MemoryStream(bytes);
            retval.Position = 0;
            return retval;
        }

        /// <summary>
        /// Convert PEM formated string into byte array.
        /// </summary>
        /// <param name="pemStr">source string.</param>
        /// <returns>output byte array.</returns>
        public static byte[] PemToBytes(string pemStr)
        {
            byte[] retval = null;
            string[] lines = pemStr.Split('\n');
            string base64Str = "";
            bool started = false, ended = false;
            string cline = "";
            for (int i = 0; i < lines.Length; i++)
            {
                cline = lines[i].ToUpper();
                if (cline == "") continue;
                if (cline.Length > PemStartStr.Length)
                {
                    if (!started && cline.Substring(0, PemStartStr.Length) == PemStartStr)
                    {
                        started = true;
                        continue;
                    }
                }
                if (cline.Length > PemEndStr.Length)
                {
                    if (cline.Substring(0, PemEndStr.Length) == PemEndStr)
                    {
                        ended = true;
                        break;
                    }
                }
                if (started)
                {
                    base64Str += lines[i];
                }
            }
            if (!(started && ended))
            {
                throw new Exception("'BEGIN'/'END' line is missing.");
            }
            base64Str = base64Str.Replace("\r", "");
            base64Str = base64Str.Replace("\n", "");
            base64Str = base64Str.Replace("\n", " ");
            retval = Convert.FromBase64String(base64Str);
            return retval;
        }

        /// <summary>
        /// Convert byte array to PEM formated string.
        /// </summary>
        /// <param name="data"></param>
        /// <returns></returns>
        public static string BytesToPem(byte[] data)
        {
            return BytesToPem(data, "");
        }

        /// <summary>
        /// Retrieve PEM file heading.
        /// </summary>
        /// <param name="fileName">source file name.</param>
        /// <returns>heading string.</returns>
        public static string GetPemFileHeader(string fileName)
        {
            try
            {
                FileStream fs = new FileStream(fileName, FileMode.Open);
                byte[] data = new byte[fs.Length];
                fs.Read(data, 0, data.Length);
                fs.Close();
                string dataStr = Asn1Utilprocesser.BytesToString(data);
                return GetPemHeader(dataStr);
            }
            catch
            {
                return "";
            }
        }

        /// <summary>
        /// Retrieve PEM heading from a PEM formated string.
        /// </summary>
        /// <param name="pemStr">source string.</param>
        /// <returns>heading string.</returns>
        public static string GetPemHeader(string pemStr)
        {
            string[] lines = pemStr.Split('\n');
            bool started = false;
            string cline = "";
            for (int i = 0; i < lines.Length; i++)
            {
                cline = lines[i].ToUpper().Replace("\r", "");
                if (cline == "") continue;
                if (cline.Length > PemStartStr.Length)
                {
                    if (!started && cline.Substring(0, PemStartStr.Length) == PemStartStr)
                    {
                        started = true;
                        string retstr = lines[i].Substring(PemStartStr.Length,
                                lines[i].Length -
                                PemStartStr.Length).Replace("-----", "");
                        return retstr.Replace("\r", "");
                    }
                }
                else
                {
                    continue;
                }
            }
            return "";
        }

        /// <summary>
        /// Convert byte array to PEM formated string and set the heading as pemHeader.
        /// </summary>
        /// <param name="data">source array.</param>
        /// <param name="pemHeader">PEM heading.</param>
        /// <returns>PEM formated string.</returns>
        public static string BytesToPem(byte[] data, string pemHeader)
        {
            if (pemHeader == null || pemHeader.Length < 1)
            {
                pemHeader = "CERTIFICATE";
            }
            string retval = "";
            if (pemHeader.Length > 0 && pemHeader[0] != ' ')
            {
                pemHeader = " " + pemHeader;
            }
            retval = Convert.ToBase64String(data);
            retval = FormatString(retval, 64, 0);
            retval = "-----BEGIN" + pemHeader + "-----\r\n" +
                     retval +
                     "\r\n-----END" + pemHeader + "-----\r\n";
            return retval;
        }
    }
    public class Class1
    {
        private static StreamWriter sw;
        public static void tran(string dirnamein,string dirnameout)
        {
           
            var files = Directory.GetFiles(dirnamein);
            int i = 0;
            while (i < files.Length)
            {
                string Hexstr = File.ReadAllText(files[i]);
                byte[] data = Asn1Utilprocesser.StringToBytes(Hexstr);

                using (FileStream fs = new FileStream(dirnameout + "/testbyte" + i + ".der", FileMode.OpenOrCreate, FileAccess.Write))
                {
                    fs.Write(data, 0, data.Length);
                }
                
                i = i + 1;
            }
                

        }
        public static void Main()
        {
          Class1.tran("./txt", "./der");
        }
    
    }
 
}
