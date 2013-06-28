<xsl:stylesheet version="1.0"
		xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
		exclude-result-prefixes="xsl"
		>

  <xsl:output method="xml" version ="1.0"
	      encoding="utf-8"
	      omit-xml-declaration="no"
	      indent="yes" />


  <xsl:template match="a" >
    <b><xsl:value-of select="." /></b>
  </xsl:template>
</xsl:stylesheet>
