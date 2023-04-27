import React, {useState} from 'react'

const FileUpload = ({onSubmit}) => {
    const [selectedFile, setSelectedFile] = useState(null);
    const handleFileSelect = (event) => {
        setSelectedFile(event.target.files[0]);
      };
      
      const handleFormSubmit = async (event) => {
        event.preventDefault();
        const formData = new FormData();
        formData.append("file", selectedFile);
        try{
          const response = await fetch("http://127.0.0.1:5000//upload-pdf", {
          method: "POST",
          body: formData,
          });
          const responseData = await response.json();
          onSubmit(responseData);
          console.log(responseData)
        } catch (error) {
        }
      };
    return (
        <form onSubmit={handleFormSubmit}>
        <input type="file" onChange={handleFileSelect} accept=".pdf" />
        <button type="submit">Upload</button>
      </form>
    )
}

export default FileUpload